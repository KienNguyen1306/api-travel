from flask import Flask,jsonify
import untils as un
app = Flask(__name__)

@app.route('/api',methods = ['GET'])
def API_PRODUCTS():
    travel = un.read_travel()
    testimonials = un.read_testimonials()
    teams =un.read_teamsdata()
    service = un.read_Service()
    posts = un.read_postData()
    asked = un.read_askedDatas()
    return jsonify({
        "travel":travel,
        "testimonials":testimonials,
        "teams":teams,
        "service":service,
        "posts":posts,
        "asked":asked
    })

@app.route('/api/travel',methods = ['GET'])
def API_traval():
    travel = un.read_travel()
    return jsonify({
        "travel":travel
})


if __name__ == '__main__':
    app.run(debug=True)