# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: _api.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder


_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 1, "", "_api.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\n_api.proto\x12\x06optuna"W\n\x15\x43reateNewStudyRequest\x12*\n\ndirections\x18\x01 \x03(\x0e\x32\x16.optuna.StudyDirection\x12\x12\n\nstudy_name\x18\x02 \x01(\t"\'\n\x13\x43reateNewStudyReply\x12\x10\n\x08study_id\x18\x01 \x01(\x03"&\n\x12\x44\x65leteStudyRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03"\x12\n\x10\x44\x65leteStudyReply"L\n\x1cSetStudyUserAttributeRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"\x1c\n\x1aSetStudyUserAttributeReply"N\n\x1eSetStudySystemAttributeRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"\x1e\n\x1cSetStudySystemAttributeReply"/\n\x19GetStudyIdFromNameRequest\x12\x12\n\nstudy_name\x18\x01 \x01(\t"+\n\x17GetStudyIdFromNameReply\x12\x10\n\x08study_id\x18\x01 \x01(\x03"-\n\x19GetStudyNameFromIdRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03"-\n\x17GetStudyNameFromIdReply\x12\x12\n\nstudy_name\x18\x01 \x01(\t"-\n\x19GetStudyDirectionsRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03"E\n\x17GetStudyDirectionsReply\x12*\n\ndirections\x18\x01 \x03(\x0e\x32\x16.optuna.StudyDirection"1\n\x1dGetStudyUserAttributesRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03"\xa6\x01\n\x1bGetStudyUserAttributesReply\x12P\n\x0fuser_attributes\x18\x01 \x03(\x0b\x32\x37.optuna.GetStudyUserAttributesReply.UserAttributesEntry\x1a\x35\n\x13UserAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"3\n\x1fGetStudySystemAttributesRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03"\xb0\x01\n\x1dGetStudySystemAttributesReply\x12V\n\x11system_attributes\x18\x01 \x03(\x0b\x32;.optuna.GetStudySystemAttributesReply.SystemAttributesEntry\x1a\x37\n\x15SystemAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x16\n\x14GetAllStudiesRequest"A\n\x12GetAllStudiesReply\x12+\n\x0e\x66rozen_studies\x18\x01 \x03(\x0b\x32\x13.optuna.FrozenStudy"V\n\x15\x43reateNewTrialRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03\x12+\n\x0etemplate_trial\x18\x02 \x01(\x0b\x32\x13.optuna.FrozenTrial"\'\n\x13\x43reateNewTrialReply\x12\x10\n\x08trial_id\x18\x01 \x01(\x03"t\n\x18SetTrialParameterRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\x03\x12\x12\n\nparam_name\x18\x02 \x01(\t\x12\x1c\n\x14param_value_internal\x18\x03 \x01(\x01\x12\x14\n\x0c\x64istribution\x18\x04 \x01(\t"\x18\n\x16SetTrialParameterReply"Q\n\'GetTrialIdFromStudyIdTrialNumberRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03\x12\x14\n\x0ctrial_number\x18\x02 \x01(\x03"9\n%GetTrialIdFromStudyIdTrialNumberReply\x12\x10\n\x08trial_id\x18\x01 \x01(\x03"a\n\x1aSetTrialStateValuesRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\x03\x12!\n\x05state\x18\x02 \x01(\x0e\x32\x12.optuna.TrialState\x12\x0e\n\x06values\x18\x03 \x03(\x01"1\n\x18SetTrialStateValuesReply\x12\x15\n\rtrial_updated\x18\x01 \x01(\x08"^\n SetTrialIntermediateValueRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\x03\x12\x0c\n\x04step\x18\x02 \x01(\x03\x12\x1a\n\x12intermediate_value\x18\x03 \x01(\x01" \n\x1eSetTrialIntermediateValueReply"L\n\x1cSetTrialUserAttributeRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\x03\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"\x1c\n\x1aSetTrialUserAttributeReply"N\n\x1eSetTrialSystemAttributeRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\x03\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"\x1e\n\x1cSetTrialSystemAttributeReply"#\n\x0fGetTrialRequest\x12\x10\n\x08trial_id\x18\x01 \x01(\x03":\n\rGetTrialReply\x12)\n\x0c\x66rozen_trial\x18\x01 \x01(\x0b\x32\x13.optuna.FrozenTrial"]\n\x13GetAllTrialsRequest\x12\x10\n\x08study_id\x18\x01 \x01(\x03\x12\x10\n\x08\x64\x65\x65pcopy\x18\x02 \x01(\x08\x12"\n\x06states\x18\x03 \x03(\x0e\x32\x12.optuna.TrialState"?\n\x11GetAllTrialsReply\x12*\n\rfrozen_trials\x18\x01 \x03(\x0b\x32\x13.optuna.FrozenTrial"\xd7\x02\n\x0b\x46rozenStudy\x12\x10\n\x08study_id\x18\x01 \x01(\x03\x12\x12\n\nstudy_name\x18\x02 \x01(\t\x12*\n\ndirections\x18\x03 \x03(\x0e\x32\x16.optuna.StudyDirection\x12@\n\x0fuser_attributes\x18\x04 \x03(\x0b\x32\'.optuna.FrozenStudy.UserAttributesEntry\x12\x44\n\x11system_attributes\x18\x05 \x03(\x0b\x32).optuna.FrozenStudy.SystemAttributesEntry\x1a\x35\n\x13UserAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15SystemAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xe7\x05\n\x0b\x46rozenTrial\x12\x10\n\x08trial_id\x18\x01 \x01(\x03\x12\x0e\n\x06number\x18\x02 \x01(\x03\x12!\n\x05state\x18\x03 \x01(\x0e\x32\x12.optuna.TrialState\x12\x0e\n\x06values\x18\x04 \x03(\x01\x12\x16\n\x0e\x64\x61tetime_start\x18\x05 \x01(\t\x12\x19\n\x11\x64\x61tetime_complete\x18\x06 \x01(\t\x12/\n\x06params\x18\x07 \x03(\x0b\x32\x1f.optuna.FrozenTrial.ParamsEntry\x12=\n\rdistributions\x18\x08 \x03(\x0b\x32&.optuna.FrozenTrial.DistributionsEntry\x12@\n\x0fuser_attributes\x18\t \x03(\x0b\x32\'.optuna.FrozenTrial.UserAttributesEntry\x12\x44\n\x11system_attributes\x18\n \x03(\x0b\x32).optuna.FrozenTrial.SystemAttributesEntry\x12H\n\x13intermediate_values\x18\x0b \x03(\x0b\x32+.optuna.FrozenTrial.IntermediateValuesEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x34\n\x12\x44istributionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13UserAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15SystemAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x39\n\x17IntermediateValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01*,\n\x0eStudyDirection\x12\x0c\n\x08MINIMIZE\x10\x00\x12\x0c\n\x08MAXIMIZE\x10\x01*J\n\nTrialState\x12\x0b\n\x07RUNNING\x10\x00\x12\x0c\n\x08\x43OMPLETE\x10\x01\x12\n\n\x06PRUNED\x10\x02\x12\x08\n\x04\x46\x41IL\x10\x03\x12\x0b\n\x07WAITING\x10\x04\x32\xe0\r\n\x0eStorageService\x12L\n\x0e\x43reateNewStudy\x12\x1d.optuna.CreateNewStudyRequest\x1a\x1b.optuna.CreateNewStudyReply\x12\x43\n\x0b\x44\x65leteStudy\x12\x1a.optuna.DeleteStudyRequest\x1a\x18.optuna.DeleteStudyReply\x12\x61\n\x15SetStudyUserAttribute\x12$.optuna.SetStudyUserAttributeRequest\x1a".optuna.SetStudyUserAttributeReply\x12g\n\x17SetStudySystemAttribute\x12&.optuna.SetStudySystemAttributeRequest\x1a$.optuna.SetStudySystemAttributeReply\x12X\n\x12GetStudyIdFromName\x12!.optuna.GetStudyIdFromNameRequest\x1a\x1f.optuna.GetStudyIdFromNameReply\x12X\n\x12GetStudyNameFromId\x12!.optuna.GetStudyNameFromIdRequest\x1a\x1f.optuna.GetStudyNameFromIdReply\x12X\n\x12GetStudyDirections\x12!.optuna.GetStudyDirectionsRequest\x1a\x1f.optuna.GetStudyDirectionsReply\x12\x64\n\x16GetStudyUserAttributes\x12%.optuna.GetStudyUserAttributesRequest\x1a#.optuna.GetStudyUserAttributesReply\x12j\n\x18GetStudySystemAttributes\x12\'.optuna.GetStudySystemAttributesRequest\x1a%.optuna.GetStudySystemAttributesReply\x12I\n\rGetAllStudies\x12\x1c.optuna.GetAllStudiesRequest\x1a\x1a.optuna.GetAllStudiesReply\x12L\n\x0e\x43reateNewTrial\x12\x1d.optuna.CreateNewTrialRequest\x1a\x1b.optuna.CreateNewTrialReply\x12U\n\x11SetTrialParameter\x12 .optuna.SetTrialParameterRequest\x1a\x1e.optuna.SetTrialParameterReply\x12\x82\x01\n GetTrialIdFromStudyIdTrialNumber\x12/.optuna.GetTrialIdFromStudyIdTrialNumberRequest\x1a-.optuna.GetTrialIdFromStudyIdTrialNumberReply\x12[\n\x13SetTrialStateValues\x12".optuna.SetTrialStateValuesRequest\x1a .optuna.SetTrialStateValuesReply\x12m\n\x19SetTrialIntermediateValue\x12(.optuna.SetTrialIntermediateValueRequest\x1a&.optuna.SetTrialIntermediateValueReply\x12\x61\n\x15SetTrialUserAttribute\x12$.optuna.SetTrialUserAttributeRequest\x1a".optuna.SetTrialUserAttributeReply\x12g\n\x17SetTrialSystemAttribute\x12&.optuna.SetTrialSystemAttributeRequest\x1a$.optuna.SetTrialSystemAttributeReply\x12:\n\x08GetTrial\x12\x17.optuna.GetTrialRequest\x1a\x15.optuna.GetTrialReply\x12\x46\n\x0cGetAllTrials\x12\x1b.optuna.GetAllTrialsRequest\x1a\x19.optuna.GetAllTrialsReplyb\x06proto3'  # noqa: E501
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "_api_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_GETSTUDYUSERATTRIBUTESREPLY_USERATTRIBUTESENTRY"]._loaded_options = None
    _globals["_GETSTUDYUSERATTRIBUTESREPLY_USERATTRIBUTESENTRY"]._serialized_options = b"8\001"
    _globals["_GETSTUDYSYSTEMATTRIBUTESREPLY_SYSTEMATTRIBUTESENTRY"]._loaded_options = None
    _globals["_GETSTUDYSYSTEMATTRIBUTESREPLY_SYSTEMATTRIBUTESENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENSTUDY_USERATTRIBUTESENTRY"]._loaded_options = None
    _globals["_FROZENSTUDY_USERATTRIBUTESENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENSTUDY_SYSTEMATTRIBUTESENTRY"]._loaded_options = None
    _globals["_FROZENSTUDY_SYSTEMATTRIBUTESENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENTRIAL_PARAMSENTRY"]._loaded_options = None
    _globals["_FROZENTRIAL_PARAMSENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENTRIAL_DISTRIBUTIONSENTRY"]._loaded_options = None
    _globals["_FROZENTRIAL_DISTRIBUTIONSENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENTRIAL_USERATTRIBUTESENTRY"]._loaded_options = None
    _globals["_FROZENTRIAL_USERATTRIBUTESENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENTRIAL_SYSTEMATTRIBUTESENTRY"]._loaded_options = None
    _globals["_FROZENTRIAL_SYSTEMATTRIBUTESENTRY"]._serialized_options = b"8\001"
    _globals["_FROZENTRIAL_INTERMEDIATEVALUESENTRY"]._loaded_options = None
    _globals["_FROZENTRIAL_INTERMEDIATEVALUESENTRY"]._serialized_options = b"8\001"
    _globals["_STUDYDIRECTION"]._serialized_start = 3545
    _globals["_STUDYDIRECTION"]._serialized_end = 3589
    _globals["_TRIALSTATE"]._serialized_start = 3591
    _globals["_TRIALSTATE"]._serialized_end = 3665
    _globals["_CREATENEWSTUDYREQUEST"]._serialized_start = 22
    _globals["_CREATENEWSTUDYREQUEST"]._serialized_end = 109
    _globals["_CREATENEWSTUDYREPLY"]._serialized_start = 111
    _globals["_CREATENEWSTUDYREPLY"]._serialized_end = 150
    _globals["_DELETESTUDYREQUEST"]._serialized_start = 152
    _globals["_DELETESTUDYREQUEST"]._serialized_end = 190
    _globals["_DELETESTUDYREPLY"]._serialized_start = 192
    _globals["_DELETESTUDYREPLY"]._serialized_end = 210
    _globals["_SETSTUDYUSERATTRIBUTEREQUEST"]._serialized_start = 212
    _globals["_SETSTUDYUSERATTRIBUTEREQUEST"]._serialized_end = 288
    _globals["_SETSTUDYUSERATTRIBUTEREPLY"]._serialized_start = 290
    _globals["_SETSTUDYUSERATTRIBUTEREPLY"]._serialized_end = 318
    _globals["_SETSTUDYSYSTEMATTRIBUTEREQUEST"]._serialized_start = 320
    _globals["_SETSTUDYSYSTEMATTRIBUTEREQUEST"]._serialized_end = 398
    _globals["_SETSTUDYSYSTEMATTRIBUTEREPLY"]._serialized_start = 400
    _globals["_SETSTUDYSYSTEMATTRIBUTEREPLY"]._serialized_end = 430
    _globals["_GETSTUDYIDFROMNAMEREQUEST"]._serialized_start = 432
    _globals["_GETSTUDYIDFROMNAMEREQUEST"]._serialized_end = 479
    _globals["_GETSTUDYIDFROMNAMEREPLY"]._serialized_start = 481
    _globals["_GETSTUDYIDFROMNAMEREPLY"]._serialized_end = 524
    _globals["_GETSTUDYNAMEFROMIDREQUEST"]._serialized_start = 526
    _globals["_GETSTUDYNAMEFROMIDREQUEST"]._serialized_end = 571
    _globals["_GETSTUDYNAMEFROMIDREPLY"]._serialized_start = 573
    _globals["_GETSTUDYNAMEFROMIDREPLY"]._serialized_end = 618
    _globals["_GETSTUDYDIRECTIONSREQUEST"]._serialized_start = 620
    _globals["_GETSTUDYDIRECTIONSREQUEST"]._serialized_end = 665
    _globals["_GETSTUDYDIRECTIONSREPLY"]._serialized_start = 667
    _globals["_GETSTUDYDIRECTIONSREPLY"]._serialized_end = 736
    _globals["_GETSTUDYUSERATTRIBUTESREQUEST"]._serialized_start = 738
    _globals["_GETSTUDYUSERATTRIBUTESREQUEST"]._serialized_end = 787
    _globals["_GETSTUDYUSERATTRIBUTESREPLY"]._serialized_start = 790
    _globals["_GETSTUDYUSERATTRIBUTESREPLY"]._serialized_end = 956
    _globals["_GETSTUDYUSERATTRIBUTESREPLY_USERATTRIBUTESENTRY"]._serialized_start = 903
    _globals["_GETSTUDYUSERATTRIBUTESREPLY_USERATTRIBUTESENTRY"]._serialized_end = 956
    _globals["_GETSTUDYSYSTEMATTRIBUTESREQUEST"]._serialized_start = 958
    _globals["_GETSTUDYSYSTEMATTRIBUTESREQUEST"]._serialized_end = 1009
    _globals["_GETSTUDYSYSTEMATTRIBUTESREPLY"]._serialized_start = 1012
    _globals["_GETSTUDYSYSTEMATTRIBUTESREPLY"]._serialized_end = 1188
    _globals["_GETSTUDYSYSTEMATTRIBUTESREPLY_SYSTEMATTRIBUTESENTRY"]._serialized_start = 1133
    _globals["_GETSTUDYSYSTEMATTRIBUTESREPLY_SYSTEMATTRIBUTESENTRY"]._serialized_end = 1188
    _globals["_GETALLSTUDIESREQUEST"]._serialized_start = 1190
    _globals["_GETALLSTUDIESREQUEST"]._serialized_end = 1212
    _globals["_GETALLSTUDIESREPLY"]._serialized_start = 1214
    _globals["_GETALLSTUDIESREPLY"]._serialized_end = 1279
    _globals["_CREATENEWTRIALREQUEST"]._serialized_start = 1281
    _globals["_CREATENEWTRIALREQUEST"]._serialized_end = 1367
    _globals["_CREATENEWTRIALREPLY"]._serialized_start = 1369
    _globals["_CREATENEWTRIALREPLY"]._serialized_end = 1408
    _globals["_SETTRIALPARAMETERREQUEST"]._serialized_start = 1410
    _globals["_SETTRIALPARAMETERREQUEST"]._serialized_end = 1526
    _globals["_SETTRIALPARAMETERREPLY"]._serialized_start = 1528
    _globals["_SETTRIALPARAMETERREPLY"]._serialized_end = 1552
    _globals["_GETTRIALIDFROMSTUDYIDTRIALNUMBERREQUEST"]._serialized_start = 1554
    _globals["_GETTRIALIDFROMSTUDYIDTRIALNUMBERREQUEST"]._serialized_end = 1635
    _globals["_GETTRIALIDFROMSTUDYIDTRIALNUMBERREPLY"]._serialized_start = 1637
    _globals["_GETTRIALIDFROMSTUDYIDTRIALNUMBERREPLY"]._serialized_end = 1694
    _globals["_SETTRIALSTATEVALUESREQUEST"]._serialized_start = 1696
    _globals["_SETTRIALSTATEVALUESREQUEST"]._serialized_end = 1793
    _globals["_SETTRIALSTATEVALUESREPLY"]._serialized_start = 1795
    _globals["_SETTRIALSTATEVALUESREPLY"]._serialized_end = 1844
    _globals["_SETTRIALINTERMEDIATEVALUEREQUEST"]._serialized_start = 1846
    _globals["_SETTRIALINTERMEDIATEVALUEREQUEST"]._serialized_end = 1940
    _globals["_SETTRIALINTERMEDIATEVALUEREPLY"]._serialized_start = 1942
    _globals["_SETTRIALINTERMEDIATEVALUEREPLY"]._serialized_end = 1974
    _globals["_SETTRIALUSERATTRIBUTEREQUEST"]._serialized_start = 1976
    _globals["_SETTRIALUSERATTRIBUTEREQUEST"]._serialized_end = 2052
    _globals["_SETTRIALUSERATTRIBUTEREPLY"]._serialized_start = 2054
    _globals["_SETTRIALUSERATTRIBUTEREPLY"]._serialized_end = 2082
    _globals["_SETTRIALSYSTEMATTRIBUTEREQUEST"]._serialized_start = 2084
    _globals["_SETTRIALSYSTEMATTRIBUTEREQUEST"]._serialized_end = 2162
    _globals["_SETTRIALSYSTEMATTRIBUTEREPLY"]._serialized_start = 2164
    _globals["_SETTRIALSYSTEMATTRIBUTEREPLY"]._serialized_end = 2194
    _globals["_GETTRIALREQUEST"]._serialized_start = 2196
    _globals["_GETTRIALREQUEST"]._serialized_end = 2231
    _globals["_GETTRIALREPLY"]._serialized_start = 2233
    _globals["_GETTRIALREPLY"]._serialized_end = 2291
    _globals["_GETALLTRIALSREQUEST"]._serialized_start = 2293
    _globals["_GETALLTRIALSREQUEST"]._serialized_end = 2386
    _globals["_GETALLTRIALSREPLY"]._serialized_start = 2388
    _globals["_GETALLTRIALSREPLY"]._serialized_end = 2451
    _globals["_FROZENSTUDY"]._serialized_start = 2454
    _globals["_FROZENSTUDY"]._serialized_end = 2797
    _globals["_FROZENSTUDY_USERATTRIBUTESENTRY"]._serialized_start = 903
    _globals["_FROZENSTUDY_USERATTRIBUTESENTRY"]._serialized_end = 956
    _globals["_FROZENSTUDY_SYSTEMATTRIBUTESENTRY"]._serialized_start = 1133
    _globals["_FROZENSTUDY_SYSTEMATTRIBUTESENTRY"]._serialized_end = 1188
    _globals["_FROZENTRIAL"]._serialized_start = 2800
    _globals["_FROZENTRIAL"]._serialized_end = 3543
    _globals["_FROZENTRIAL_PARAMSENTRY"]._serialized_start = 3273
    _globals["_FROZENTRIAL_PARAMSENTRY"]._serialized_end = 3318
    _globals["_FROZENTRIAL_DISTRIBUTIONSENTRY"]._serialized_start = 3320
    _globals["_FROZENTRIAL_DISTRIBUTIONSENTRY"]._serialized_end = 3372
    _globals["_FROZENTRIAL_USERATTRIBUTESENTRY"]._serialized_start = 903
    _globals["_FROZENTRIAL_USERATTRIBUTESENTRY"]._serialized_end = 956
    _globals["_FROZENTRIAL_SYSTEMATTRIBUTESENTRY"]._serialized_start = 1133
    _globals["_FROZENTRIAL_SYSTEMATTRIBUTESENTRY"]._serialized_end = 1188
    _globals["_FROZENTRIAL_INTERMEDIATEVALUESENTRY"]._serialized_start = 3486
    _globals["_FROZENTRIAL_INTERMEDIATEVALUESENTRY"]._serialized_end = 3543
    _globals["_STORAGESERVICE"]._serialized_start = 3668
    _globals["_STORAGESERVICE"]._serialized_end = 5428
# @@protoc_insertion_point(module_scope)
