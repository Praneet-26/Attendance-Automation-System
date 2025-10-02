# import boto3, tempfile, json
# from deepface import DeepFace

# s3 = boto3.client("s3")
# dynamodb = boto3.resource("dynamodb")
# students_table = dynamodb.Table("Students")

# def lambda_handler(event, context):
#     for record in event["Records"]:
#         bucket = record["s3"]["bucket"]["name"]
#         key = record["s3"]["object"]["key"]

#         # Download photo locally
#         with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
#             s3.download_file(bucket, key, tmp_file.name)

#             # Extract face embedding
#             try:
#                 embedding = DeepFace.represent(img_path=tmp_file.name, model_name="Facenet")[0]["embedding"]

#                 # Extract student_id from key (prefix: students/{student_id}/...)
#                 student_id = key.split("/")[1]

#                 # Update DynamoDB with embedding
#                 students_table.update_item(
#                     Key={"student_id": student_id},
#                     UpdateExpression="SET photo_url = :url, embedding = :embedding",
#                     ExpressionAttributeValues={
#                         ":url": f"s3://{bucket}/{key}",
#                         ":embedding": embedding
#                     }
#                 )

#                 print(f"Student {student_id} photo registered with embedding")

#             except Exception as e:
#                 print(f"Failed to process {key}: {str(e)}")

#     return {"statusCode": 200, "body": json.dumps("Processed student photos")}
