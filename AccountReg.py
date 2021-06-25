import cx_Oracle
import json
import requests
import uuid
import Utility
import Connection
from datetime import datetime

accountUrl = "https://account-reg-dev01.dev01.apigw.tds.net"
tablename = "salesforce_migr.SDM_SF_ACCOUNT_REGISTRY"


class Account(object):
    def __init__(self, uuid=None, attrs=None, rels=None, acctTp=None, effTm=None, createdTm=None, parentId=None, rootId=None):
        self.uuid = uuid
        self.attrs = attrs
        self.rels = rels
        self.acctTp = acctTp
        self.effTm = effTm
        self.createdTm = createdTm
        self.parentId = parentId
        self.rootId = rootId

    def __dict__(self):
        dic = {"accountType": self.acctTp, "effectiveTime": str(
            self.effTm), "attributes": self.attrs, "relationships": self.rels}
        if self.uuid is not None:
            dic["tdsAccountUuid"] = self.uuid
        if self.parentId is not None:
            dic["parentTdsAccountUuid"] = self.uuid
        if self.rootId is not None:
            dic["rootTdsAccountUuid"] = self.uuid
        return dic

    def printJson(self):
        print(json.dumps(self.__dict__()))

    def processAccount(self):
        global accountUrl
        url = "{}/v1/account".format(accountUrl)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Tds-Transaction-ID": str(uuid.uuid4()),
            # may want to use cmd line arg for this
            "X-Tds-Originating-Username": "usrulu",
            "X-Tds-Originating-User-Type": "tds-employee",
            "X-Tds-Requesting-Timestamp": str(datetime.now()),
            "X-Tds-Originating-Network-Address": str(
                Utility.get_ip()),
            "X-Tds-Originating-System-Name": "Data Migration",
            # will need to change this based on host name
            "X-Tds-Requesting-System-Hostname": "pocgen0.sec.tds.net"
        }
        payload = json.dumps(self.__dict__())

        req = requests.post(url=url, headers=headers, json=payload)
        jsonResp = json.loads(req.text)
        acctUuid = jsonResp["tdsAccountUuid"]

        cur = Connection.getCursor()
        cur.execute(
            "update {} set TDS_ACCOUNT_UUID = :1 where SF_ACCOUNT_REGISTRY_ID = :2".format(tablename), self.uuid, self.id)
