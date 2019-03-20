from peewee import * 

db = SqliteDatabase('database.db') #find a better way to do this?

class Experiment(Model):
    name = CharField()
    execution_id = TextField()
    timestamp = BigIntegerField()

    class Meta:
        database = db

class ParamMetric(Model):
    assignee = CharField(null=True)
    keyword_name = CharField(null=True)
    value = CharField(null=True)
    var_type = CharField()
    runtime_val = CharField()
    execution_id = ForeignKeyField(Experiment, to_field='execution_id')
    from_id = BigIntegerField(null = True)
    path_id = BigIntegerField(null = True)
    trial_id = BigIntegerField(null = True)

    class Meta:
       database = db

class ReadWrite(Model):
    execution_id = ForeignKeyField(Experiment, to_field='execution_id')
    file_path = CharField()
    rw = CharField()

    class Meta:
        database = db

def insert_experiment(n:str, exec:str, ts:int):
    try:
        exp = Experiment.get(Experiment.name == n, Experiment.execution_id == exec);
        #do we want timestamp updated?
        return
    except:
        exp = Experiment.create(name = n, execution_id = exec, timestamp = ts)
        exp.save()

def insert_ParamMetric(a:str, kw_name:str, val:str, type:str, r_val:str, exec:str, path:int, trial:int):
    pm = ParamMetric.create(assignee=a, keyword_name=kw_name, value=val, var_type=type, runtime_val=r_val,
                       execution_id=exec, path_id=path, trial_id=trial)
    pm.save()

def insert_rw(exec:str, fp:str, rw:str):
    r_w = ReadWrite.create(execution_id = exec, file_path = fp, rw = rw)
    r_w.save()


db.connect()
db.create_tables([Experiment, ParamMetric, ReadWrite])