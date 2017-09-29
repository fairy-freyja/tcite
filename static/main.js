  function showBlock(blockName){
  var len = $(".content").length
	for(var i = 0; i< len; i++){
		$(".content")[i].style.display = 'none';
	}
	$(blockName).show();
  }
