import run
from Restconnector import RestConnector
from qc_client import QcClient
from quality_center_utils import UpdateIterations
import constants
from base_entity import BaseEntity
from MyEntity import *


client=QcClient(username='slyusarev.aa@edu.spbstu.ru',password='Kaga5xa1')

client.Login()

print(client.GetEntity(entityType="tests"))
print(client.GetEntity(entityType="tests",entityId=214))
print(client.GetTestById(214))
print(client.GetTestByName('Test1'))
print(client.GetTestSetFolderByName("f1"))
a={u'text-sync': None, u'user-01': u'Reviewed', u'user-03': u'2-Medium', u'vc-start-audit-action-id': u'6864', u'ver-stamp': u'53', u'has-linkage': u'N', u'has-dependencies': u'0', u'configurations-count': u'2', u'base-test-id': None, u'owner': None, u'estimate-devtime': None, u'id': u'214', u'vc-time': None, u'vc-comments': None, u'vc-end-audit-action-id': u'6864', u'vc-version-number': None, u'parent-id': u'1175', u'exec-status': u'No Run', u'attachment': None, u'template': None, u'step-param': u'0', u'has-criteria': u'N', u'runtime-data': None, u'status': u'Design', u'creation-time': u'2018-07-15', u'user-02': None, u'vc-checkin-time': None, u'description': None, u'subtype-id': u'MANUAL', u'vc-checkin-comments': None, u'last-modified': u'2018-07-25 11:56:16', u'vc-checkin-user-name': None, u'order-id': u'1', u'vc-status': None, u'name': u'Test1', u'dev-comments': None, u'storage-path': None, u'steps': u'3', u'timeout': None, u'user-04': u'Basic', u'vc-checkin-date': None, u'check-out-user-name': None, u'vc-date': None}
client.UpdateEntity("tests",a,214)
print(client.GetTestByName('Test1'))
print(client.GetRuns())
print(client.GetRuns(410))
print(client.GetTestConfigs(214))
print(client.GetTestConfigById(1216))
print(client.GetTestParameters(214))
print(client.GetTestSetByName("Validation"))
print(client.GetTestSetFoldersById(10))
print(client.GetTestSetById(308))
print(client.GetTestSetByParentId(26))
print(client.GetTestSetFoldersByParentId(9))
print(client.GetReleaseCyclesByDates(1001,"2018-07-25", "2034-07-25"))
print(client.GetTestInstances(308))
print(client.GetTestInstances())
print(client.GetMandatoryFields("runs"))
print(client.GetMandatoryFields("tests"))
print(client.GetMandatoryFields("test-configs"))
print(client.GetMandatoryFields("test-sets"))
print(client.GetMandatoryFields("test-configs"))
print(client.GetMandatoryFields("test-set-folders"))
print(client.GetMandatoryFields("test-instances"))
print(client.GetMandatoryFields("release-cycles"))
print(client.GetMandatoryFields("defects"))


cc=TestSet("FirstSet1")
print(client.CreateEntity("test-sets",cc))

cc=TestInstance(testId=214,cycleId=0)
print(client.CreateEntity("test-instances",cc))

cc=Test("Basic","1-Low","Reviewed","1175","Test#!1","MANUAL")
print(client.CreateEntity("tests",cc))

cc=TestConfigs("Test1","214")
print(client.CreateEntity("test-config",cc))

cc=TestSetFolders("ExampleFolder1")
print(client.CreateEntity("test-set-folder",cc))


cc=ReleaseCycle("2018-07-29","ExampleCycle1",1001,"2018-07-25")
print(client.CreateEntity("release-cycle",cc))

cc=Runs("Test1",214,1001,"")
print(client.CreateEntity("run",cc))

cc=TestInstance(testId=214,cycleId=0)
print(client.CreateTestInstance(cc))


cc=TestSet("FirstSet1")
print(client.CreateTestSet(cc))

v=run.Run()
client.CreateTestRun(run=v,status="1-Low",instanceDataToUpdate=a)


print(client.GetTestObjByTcId(214))


print(client.GetFields(entityType="test-set-folder"))
