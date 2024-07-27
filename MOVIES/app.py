from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pre-trained model and data
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form['movie_title']
    index = movies[movies['title'] == movie_title].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movies = []
    for i in distance[0:1500]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return render_template('recommendations.html', recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)