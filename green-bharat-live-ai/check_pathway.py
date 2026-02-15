try:
    import pathway as pw
    print(f"Pathway version: {pw.__version__}")
    if hasattr(pw, 'io') and hasattr(pw.io, 'csv'):
        print("Pathway IO modules available.")
    else:
        print("Pathway IO modules NOT available.")
except Exception as e:
    print(f"Error: {e}")
