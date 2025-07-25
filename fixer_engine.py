
def diagnose_issue(text):
    # Simple keyword-based logic for demo
    if "GL" in text or "journal" in text:
        return "GL Issue detected. Suggest checking your Journal Category, Ledger setup, and FSM mapping rules."
    elif "OIC" in text:
        return "OIC Issue: Try restarting the failed integration instance via /ic/api/integrations."
    elif "FBDI" in text:
        return "FBDI Error: Validate your CSV template, ensure required columns are filled."
    elif "AP" in text:
        return "AP Invoice Issue: Check supplier config, matching rules, and PO linkage."
    return "No known Oracle issue pattern detected. Please refine the input or add more details."
