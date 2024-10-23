WEB APP:

Chapter 9: Embedding a Machine Learning Model into a Web Application Serializing fitted scikit-learn estimators Setting up a SQLite database for data storage Developing a web application with Flask Our first Flask web application Form validation and rendering Turning the movie classifier into a web application Deploying the web application to a public server Updating the movie review classifier

Raschka, Sebastian. Python Machine Learning : Learn How to Build Powerful Python Machine Learning Algorithms to Generate Useful Data Insights with This Data Analysis Tutorial, Packt Publishing, Limited, 2015. ProQuest Ebook Central, http://ebookcentral.proquest.com/lib/bibliouocsp-ebooks/detail.action?docID=4191233.
Created from bibliouocsp-ebooks on 2024-04-04 10:27:01.


Animation:

https://github.com/oreillymedia/t-SNE-tutorial?tab=readme-ov-file 

We create an animation using MoviePy.

f, ax, sc, txts = scatter(X_iter[..., -1], y)

def make_frame_mpl(t):
    i = int(t*40)
    x = X_iter[..., i]
    sc.set_offsets(x)
    for j, txt in zip(range(10), txts):
        xtext, ytext = np.median(x[y == j, :], axis=0)
        txt.set_x(xtext)
        txt.set_y(ytext)
    return mplfig_to_npimage(f)

animation = mpy.VideoClip(make_frame_mpl,
                          duration=X_iter.shape[2]/40.)
animation.write_gif("images/animation.gif", fps=20)

We can clearly observe the different phases of the optimization, as described in the original paper.

Let's also create an animation of the similarity matrix of the map points. We'll observe that it's getting closer and closer to the similarity matrix of the data points.

n = 1. / (pdist(X_iter[..., -1], "sqeuclidean") + 1)
Q = n / (2.0 * np.sum(n))
Q = squareform(Q)

f = plt.figure(figsize=(6, 6))
ax = plt.subplot(aspect='equal')
im = ax.imshow(Q, interpolation='none', cmap=pal)
plt.axis('tight')
plt.axis('off')

def make_frame_mpl(t):
    i = int(t*40)
    n = 1. / (pdist(X_iter[..., i], "sqeuclidean") + 1)
    Q = n / (2.0 * np.sum(n))
    Q = squareform(Q)
    im.set_data(Q)
    return mplfig_to_npimage(f)

animation = mpy.VideoClip(make_frame_mpl,
                          duration=X_iter.shape[2]/40.)
animation.write_gif("images/animation_matrix.gif", fps=20)