import json
from flask import Flask, request

app = Flask(__name__)

# This route handles POST requests to the /parse endpoint.
@app.route("/parse", methods=["POST"])
def lookup(input_json=None):

    # The `input_json` parameter is optional.
    # If the parameter is not passed, the function will get the JSON data
    # from the request body.

    # Get the JSON data from the request body.
    if input_json is None:
        json_data = request.get_json()

    # The `json_data` variable contains the JSON data
    # that was sent in the request.

    # Look up the specified fields.
    data_first_frame_number = json_data["FirstFrame"]
    data_last_frame_number = json_data["LastFrame"]

    # The `data_first_frame_number` and
    # `data_last_frame_number` variables contain the first and last frame numbers
    # that were specified in the request.

    # Read the data from the Input.json file
    with open("Input.json") as f:
        data = json.load(f)

    # The `data` variable contains the data from the
    # Input.json file.

    # Convert the first and last frame numbers to integers.
    first_frame_number = data["FirstFrameNumber"]
    last_frame_number = data["LastFrameNumber"]

    # The `first_frame_number_as_int` and
    # `last_frame_number_as_int` variables contain the first and last frame numbers
    # as integers.

    # Create the new filenames by replacing the "%07d" placeholder with the
    # first and last frame numbers, respectively.
    first_frame_number_as_int = int(first_frame_number)
    last_frame_number_as_int = int(last_frame_number)

    # The `first_frame_number_as_int` and
    # `last_frame_number_as_int` variables contain the first and last frame numbers
    # as integers.

    # Create the new filenames by replacing the "%07d" placeholder with the
    # first and last frame numbers, respectively.
    new_filename_1 = data["Filename"] % first_frame_number_as_int
    new_filename_2 = data["Filename"] % last_frame_number_as_int

    # The `new_filename_1` and `new_filename_2`
    # variables contain the new filenames.

    # Check if the payload is correct
    if data_first_frame_number == first_frame_number_as_int and \
        data_last_frame_number == last_frame_number_as_int:
        # The `data_first_frame_number` and
        # `data_last_frame_number` variables are compared to the
        # `first_frame_number_as_int` and `last_frame_number_as_int` variables
        # to check if the payload is correct.

        # Create the output JSON object.
        output_json = {
            "FirstFrame": new_filename_1,
            "LastFrame": new_filename_2,
        }

        # Write the output JSON object to the output.json file.
        with open("output.json", "w") as f:
            json.dump(output_json, f)
        
        # Return the output JSON object and a status code of 200.
        return json.dumps(output_json), 200
    else:
        # The `return` statement returns an error message
        # and a status code of 400 if the payload is incorrect.
        return { "message": "Check the payload!"}, 400


if __name__ == "__main__":
    app.run(debug=True)
