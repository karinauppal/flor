from typing import List, Dict, Any
from flor.context.tables import *
import pandas as pd
import numpy as np
import os
import git
import json

class Node:

    def __init__(self, d):
        self.assignee = d['assignee']
        self.caller = d['caller']
        self.from_arg = d['from_arg']
        self.in_execution = d['in_execution']
        self.in_file = d['in_file']
        self.instruction_no = d['instruction_no']
        self.keyword_name = d['keyword_name']
        self.pos = d['pos']
        self.runtime_value = d['runtime_value']
        self.typ = d['typ']
        self.value = d['value']
        self.stack_frame = d['__stack_frame__']

        self.children = []
        self.parent = None
        self.identity = None

class Tree:

    def __init__(self, log_records: List[Dict[str, Any]]):
        self.producers_table = {}
        self.leaves = set([])
        self.build_tree(log_records)
        self.d = {}

    def build_tree(self, log_records: List[Dict[str, Any]]):
        self.producers_table = {}
        self.leaves = set([])
        marker = {}
        stack_frames = []
        nodes : List[Node] = []

        if not os.path.exists('next_id.txt'):
            with open('next_id.txt', 'w') as f:
                f.write('0')

        for r in log_records:
            if 'from' in r and 'to' in r:
                if r['to'] not in self.producers_table:
                    self.producers_table[r['to']] = set(r['from'])
                else:
                    self.producers_table[r['to']] |= set(r['from'])
            else:
                nodes.append(Node(r))
                self.leaves |= {nodes[-1],}

        for idx, node in enumerate(nodes): #figure out how to change this part
            # Attach this node to its parent, unless this node is root
            check = False
            if str(node.stack_frame) not in marker:
                # Update the marker and stack frames the first time we see a new stack_frame
                marker[str(node.stack_frame)] = node
                if stack_frames:
                    for stack_frame in stack_frames:
                        if self.__is_ancestor__(stack_frame, node.stack_frame):
                            parent = marker[str(stack_frame)]
                            parent.children.append(node)
                            node.parent = parent
                            self.leaves -= {parent,}
                            break
                stack_frames.insert(0, node.stack_frame)
            else:
                # Advance the marker
                if (node.stack_frame != nodes[-1].stack_frame and
                        self.__is_ancestor__(node.stack_frame, nodes[-1].stack_frame)):
                    # print(idx)
                    marker = {}
                    stack_frames = [node.stack_frame]
                parent = nodes[idx - 1]
                parent.children.append(node)
                node.parent = parent
                self.leaves -= {parent,}
                marker[str(node.stack_frame)] = node

        #inserting into database
        if not os.path.exists('trials.json'):
            trials = {}
        else:
            trials = json.loads(open('trials.json').read())

        commit = str(git.Repo(os.getcwd()).head.commit)
        name = git.Repo(os.getcwd()).head.commit.message
        check = insert_experiment(name, commit, 0) #fix with real timestamp later
        if check:
            trials[commit] = 0
        else:
            trials[commit] += 1 #this should already exist in the directory

        with open('next_id.txt', 'r') as f:
            identity = int(f.read())

        for node in nodes:
            if node.typ == 'read' or node.typ == 'write':
                insert_rw(identity, commit, node.value , node.typ)
            else:
                insert_ParamMetric(identity, node.assignee, node.keyword_name, node.value, node.typ,
                                   node.runtime_value, commit, None, None, trials[commit])
                #right now path_id and parent_id is empty
            identity += 1
        with open('next_id.txt', 'w') as f:
            f.write(str(identity))
        with open('trials.json', 'w') as f:
            json.dump(trials, f)

    def get_df(self):
        matrix = {}
        for col_id, leaf in enumerate(self.leaves):
            node = leaf
            while node:
                row_id = ' || '.join([str(node.assignee), str(node.keyword_name), str(node.value)])
                if row_id not in matrix:
                    matrix[row_id] = {}
                matrix[row_id][col_id] = node.runtime_value
                node = node.parent
        for row_id in matrix:
            if row_id in self.d:
                column = self.d[row_id]
            else:
                column = []
            for col_id in range(len(self.leaves)):
                if col_id not in matrix[row_id]:
                    column.append(np.nan)
                else:
                    column.append(matrix[row_id][col_id])
            self.d[row_id] = column

        return pd.DataFrame.from_dict(self.d, orient='index')

    def __is_ancestor__(self, stack_frame1, stack_frame2):
        #stack_frame 1 is earlier than stack_frame2
        if stack_frame1 == stack_frame2[0:len(stack_frame1)]:
            return True
        if stack_frame1[0:-1] == stack_frame2[0:-1]:
            # TODO: This is an overly-conservative lineage check, generalize
            n1, v1 = stack_frame1[-1]
            n2, v2 = stack_frame2[-1]
            if n1 == n2 and n1 == "function_body":
                return v1 in self.producers_table[v2]
        
        return False
