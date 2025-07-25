
def diagnose_issue(text):
    if "ORA" in text:
        return "Detected Oracle Database Error. Suggest checking SQL syntax or permissions."
    elif "OIC" in text:
        return "Issue related to Oracle Integration Cloud. Check integration instance and payload."
    else:
        return "Generic error. Please verify logs and consult Oracle docs."
