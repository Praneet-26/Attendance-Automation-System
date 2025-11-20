
provider "aws" {
  region = "us-east-1"
}

#Creating s3 bucket to upload the student image in a s3 bucket.
resource "aws_s3_bucket" "new-student-registration-tff" {
  bucket = "studentimages"
  force_destroy = true

  tags = {
    Name        = "new-student-registration-tff"
    Environment = "Dev"
  }
}

#Creating bucket for student attendace authentication
resource "aws_s3_bucket" "class-images-tff" {
  bucket = "classphotos"
   force_destroy = true

  tags = {
    Name        = "class-images-tff"
    Environment = "Dev"
  }
}



