from peewee import * 

db = SqliteDatabase('database.db') #find a better way to do this?

class Experiment(Model):
    name = CharField()
    execution_id = TextField()
    timestamp = BigIntegerField()

    class Meta:
        database = db

class Identities(Model):
    entry_id = BigIntegerField(primary_key=True)

    class Meta:
        database = db

class ParamMetric(Model):
    entry_id = ForeignKeyField(Identities)
    assignee = CharField(null=True)
    keyword_name = CharField(null=True)
    value = CharField(null=True)
    var_type = CharField()
    runtime_val = CharField()
    execution_id = ForeignKeyField(Experiment, to_field='execution_id')
    from_id = ForeignKeyField(Identities, null=True)
    path_id = BigIntegerField(null=True)
    trial_id = BigIntegerField(null=True)

    class Meta:
       database = db

class ReadWrite(Model):
    entry_id = ForeignKeyField(Identities)
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
        Experiment.create(name = n, execution_id = exec, timestamp = ts)

def insert_ParamMetric(e_id:int, a:str, kw_name:str, val:str, type:str, r_val:str, exec:str, from_id:int, path:int, trial:int):
    Identities.create(entry_id=e_id)
    ParamMetric.create(entry_id=e_id, assignee=a, keyword_name=kw_name, value=val, var_type=type, runtime_val=r_val,
                       execution_id=exec, from_id= from_id, path_id=path, trial_id=trial)

def insert_rw(e_id:int, exec:str, fp:str, rw:str):
    Identities.create(entry_id=e_id)
    ReadWrite.create(entry_id=e_id, execution_id = exec, file_path = fp, rw = rw)


db.connect()
db.create_tables([Experiment, Identities, ParamMetric, ReadWrite])