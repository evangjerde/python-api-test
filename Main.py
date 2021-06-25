import Connection
import AccountReg


def main():
    print("Starting Registry API Calls")
    username = "salesforce_migr_poc"
    password = "xxxx"
    dsn = "//RACDEV06.TDS.LOCAL:1521/DB070A1"
    tablespace = "salesforce_migr"
    # Connection.connect(username, password, dsn)
    # cur = Connection.getCursor()
    # if cur is None:
    #     print("Could Not Connect To Database")
    #     exit(1)

    # fields = "SF_ACCOUNT_REGISTRY_ID, SF_ACCOUNT_TYPE, SF_ACCOUNT_EFF_DATE, SF_ATTRIBUTE_SOURCE, SF_ATTRIBUTE_KEY, SF_ATTRIBUTE_VALUE, SF_RELATIONSHIP_SOURCE, SF_RELATIONSHIP_KEY, SF_RELATIONSHIP_VALUE"
    table = AccountReg.tablespace
    # where = "TDS_ACCOUNT_UUID IS NULL"

    # query = "SELECT {0} FROM {1} WHERE {2}".format(fields, table, where)

    # for row in cur.execute(query):
    #     id = row[0]
    #     tp = row[1]
    #     effDate = str(row[2])
    #     attrSource = row[3]
    #     attrKey = row[4]
    #     attrVal = row[5]
    #     relSource = row[6]
    #     relKey = row[7]
    #     relVal = row[8]
    #     attrs = [{"source": attrSource, "key": attrKey,
    #               "value": attrVal, "effectiveTime": effDate}]
    #     rels = [{"source": relSource, "key": relKey,
    #              "value": relVal, "effectiveTime": effDate}]
    #     acct = AccountReg.Account(
    #         attrs=attrs, rels=rels, acctTp=tp, effTm=effDate)
    #     acct.printJson()

    acct = AccountReg.Account()
    acct.processAccount()


if __name__ == "__main__":
    main()
