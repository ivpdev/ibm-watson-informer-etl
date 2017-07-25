fs = require('fs');


let INPUT_FILE='../data/posts.json';
let OUTPUT_DIR='../data/posts/';

let posts = require(INPUT_FILE)


posts.forEach(function(post) {
	let id = post.Id;

	writeFile(id + '.json', JSON.stringify(post));

});

function writeFile(name, content) {
	fs.writeFile(OUTPUT_DIR + name, content, function(err) {
	    if(err) {
	        return console.log(err);
	    }
	}); 
}

