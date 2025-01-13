from fastapi import HTTPException,UploadFile
import tempfile

# Helper function to handle the lifecycle of the temporary CSV file

async def handle_temp_csv(csv_file: UploadFile) -> str:
    try:
        # Save the uploaded CSV to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_csv:
            temp_csv.write(await csv_file.read())
            temp_csv_path = temp_csv.name
        return temp_csv_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving CSV: {str(e)}")