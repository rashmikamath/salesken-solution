from flask import Flask, escape, request, jsonify
from semantic_similarity import get_clusters

app = Flask(__name__)

@app.route('/semantic-similarity/', methods=['POST'])
def create_task():
	request_json = request.json
	valid = False
	# Basic validation
	if "input_list" in request_json and type(request_json["input_list"]) == list:
		valid = True

	sentence_array = request_json.get('input_list')
	result = get_clusters(sentence_array)

	if not valid:
		abort(400)

	return jsonify({'result': result}), 201


if __name__ == '__main__':
    app.run(debug=True)
