from flask import Flask, render_template, request
import pickle
import numpy as np

top_fifty = pickle.load(open('top_fifty.pkl', 'rb'))
idlist = pickle.load(open('idlist.pkl', 'rb'))
book1 = pickle.load(open('book1.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))


app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html',
                           book_name=list(top_fifty['title'].values),
                           author=list(top_fifty['authors'].values),
                           image=list(top_fifty['image_url'].values),
                           rating=list(top_fifty['average_rating'].values),
                           rating_count=list(top_fifty['ratings_count'].values),
                           )

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/critics')
def critics():
    return render_template('critics.html')


@app.route('/recommend_reviews', methods=['POST'])
def recommend_reviews():
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        book_list = []
        book_id = book1[book1['title'] == user_input].index
        book_id = book_id[0]

        for new in idlist[book_id]:
            list = []
            list.append(book1.loc[new].title)
            list.append(book1.loc[new].authors)
            list.append(book1.loc[new].image_url)
            list.append(book1.loc[new].average_rating)
            list.append(book1.loc[new].ratings_count)
            list.append(int(book1.loc[new].original_publication_year))
            book_list.append(list)
        print(book_list)
    return render_template('reviews.html', data=book_list)
   



@app.route('/recommend_critics', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:7]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('critics.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)