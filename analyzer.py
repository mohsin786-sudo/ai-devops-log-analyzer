def analyze_log(log_text):

    if "error" in log_text.lower():
        return {
            "status": "Failed",
            "error_detected": True,
            "summary": "Log contains an error.",
            "suggestion": "Check build configuration or dependencies."
        }
    else:
        return {
            "status": "Success",
            "error_detected": False,
            "summary": "Build passed successfully.",
            "suggestion": "No action needed."
        }
