const blog_entry = (post) => `<li style="list-style: none">
				<a href="/blog/${post.id}/">
				<div class="content" style="position: relative">
					<div id="upvote" style="position: absolute; bottom: 20px; right: 20px">
						<div id="upvote-counter">${post.upvotes}</div>
						<img src="/static/blog/images/heart.png" id="heart" />
					</div>
					<h1>${post.title}</h1>
					<ul>
						<li>${post.first_sentence}</li>
						<li id="time">Posted on the ${post.pub_date}.</li>
						<li>${post.get_comment_amount} comments</li>
					</ul>
				</div>
			</a>
		</li>`;

$(document).ready(function () {
	$.get("/blog/get_posts/10", function (data) {
		data.data.map((post) => {
			$(".post-container").append(blog_entry(post));
		});
	});
});
