import unittest
import json

from flask import Flask, jsonify, request

class TestParse(unittest.TestCase):

    def test_parse_valid_data(self):
        # Create a Flask application.
        app = Flask(__name__)

        # Define a route that parses a JSON payload and returns the new filenames.
        @app.route("/parse", methods=["POST"])
        def parse():
            """
            Parse a JSON payload and return the new filenames.

            Args:
                data: The JSON payload.

            Returns:
                A JSON object with the new filenames.
            """
            
            # Get the data from the request.
            data = request.get_json()

            # Get the first and last frame numbers from the data.
            first_frame_number = data["FirstFrameNumber"]
            last_frame_number = data["LastFrameNumber"]

            # Create the new filenames by replacing the "%07d" placeholder with the
            # first and last frame numbers, respectively.
            new_filename_1 = data["Filename"] % first_frame_number
            new_filename_2 = data["Filename"] % last_frame_number

            # Create a JSON object with the new filenames.
            output_json = {
                "FirstFrame": new_filename_1,
                "LastFrame": new_filename_2,
            }

            # Return the JSON object.
            return jsonify(output_json)

        # Create a test client for the Flask application.
        client = app.test_client()

        # Valid data
        input_json = {
            "Filename": "/Volumes/MD_1717/CF_CATS_ARI_Test/B077R0EC/B077C002_190201_R0EC/B077C002_190201_R0EC.%07d.ari",
            "FirstFrameNumber": 1235386,
            "LastFrameNumber": 1240067
        }

        # Send a POST request to the "/parse" route with the valid data.
        response = client.post("/parse", data=json.dumps(input_json), headers={"Content-Type": "application/json"})

        # Get the response data.
        json_data = response.get_data()

        # Load the response data into a JSON object.
        parsed_json = json.loads(json_data)

        # Assert that the response data is as expected.
        self.assertEqual(parsed_json, {
            "FirstFrame": "/Volumes/MD_1717/CF_CATS_ARI_Test/B077R0EC/B077C002_190201_R0EC/B077C002_190201_R0EC.1235386.ari",
            "LastFrame": "/Volumes/MD_1717/CF_CATS_ARI_Test/B077R0EC/B077C002_190201_R0EC/B077C002_190201_R0EC.1240067.ari"
        })
