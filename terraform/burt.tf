provider "aws" {
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
    region = "${var.region}"
}

resource "aws_dynamodb_table" "basic-dynamodb-table" {
    name = "BURT"
    read_capacity = 1
    write_capacity = 1
    hash_key = "domain"
    attribute {
        name = "domain"
        type = "S"
    }
    attribute {
	name = "forward"
	type = "S"
    }
    global_secondary_index {
	name = "forward_index"
	hash_key = "forward"
	projection_type = "KEYS_ONLY"
	read_capacity = 1
	write_capacity = 1
    }
}
