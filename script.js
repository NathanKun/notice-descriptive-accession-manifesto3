$(function() {
	$('#content').load("merge.html", function() {
		$('.result').click(function(ev) {
			const originDiv = $($(ev.currentTarget).siblings()[0]);
			if (originDiv.css('display') === 'none') {
				originDiv.css('display', 'block');
			} else {
				originDiv.css('display', 'none');
			}
		});
		$('.origin').click(function(ev) {
			$(ev.currentTarget).css('display', 'none');
		});
	});
})