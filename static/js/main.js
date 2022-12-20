/* $(document).ready(function(){
    
    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    
    $(".next").click(function(){
        
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();
        
        //Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
        //show the next fieldset
        next_fs.show(); 
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // for making fielset appear animation
                opacity = 1 - now;
    
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({'opacity': opacity});
            }, 
            duration: 600
        });
    });
    
    $(".previous").click(function(){
        
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();
        
        //Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
        
        //show the previous fieldset
        previous_fs.show();
    
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // for making fielset appear animation
                opacity = 1 - now;
    
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({'opacity': opacity});
            }, 
            duration: 600
        });
    });
    
    $('.radio-group .radio').click(function(){
        $(this).parent().find('.radio').removeClass('selected');
        $(this).addClass('selected');
    });
    
    $(".submit").click(function(){
        return false;
    })
        
    }); */


/* start progress bar */

const one = document.querySelector(".one");

const two = document.querySelector(".two");

const three = document.querySelector(".three");

const four = document.querySelector(".four");

const five = document.querySelector(".five");



one.onclick = function() {

    one.classList.add("active");

    two.classList.remove("active");

    three.classList.remove("active");

    four.classList.remove("active");

    five.classList.remove("active");

}


two.onclick = function() {

    one.classList.add("active");

    two.classList.add("active");

    three.classList.remove("active");

    four.classList.remove("active");

    five.classList.remove("active");

}

three.onclick = function() {

    one.classList.add("active");

    two.classList.add("active");

    three.classList.add("active");

    four.classList.remove("active");

    five.classList.remove("active");

}

four.onclick = function() {

    one.classList.add("active");

    two.classList.add("active");

    three.classList.add("active");

    four.classList.add("active");

    five.classList.remove("active");

}

five.onclick = function() {

    one.classList.add("active");

    two.classList.add("active");

    three.classList.add("active");

    four.classList.add("active");

    five.classList.add("active");

}

/* end progress bar */

/* start preview */

function cut_o() {
    var x = document.getElementById('cut_o');
    if (x.style.display === 'none') {
      x.style.display = 'block';
    } 
    else {
      x.style.display = 'none';
    }
  }
  
  function cut_m() {
    var x = document.getElementById('cut_m');
    if (x.style.display === 'none') {
      x.style.display = 'block';
    } 
    else {
      x.style.display = 'none';
    }
  }

/* end preview */

/* start templates */


function select_template(){
    var x = document.getElementById('all-templates');
    var y = document.getElementById('create-template');
    if (x.style.display === 'none') {
      y.style.display = 'none'
      x.style.display = 'block';
    } 
    else {
      x.style.display = 'none';
    }
  }
  
  function create_template(){
    var x = document.getElementById('create-template');
    var y = document.getElementById('all-templates');
    if (x.style.display === 'none') {
      x.style.display = 'block';
      y.style.display ='none'
    }
    else {
      x.style.display = 'none';
    }
  }
  
  function temp_1_1(){
    var x = document.getElementById('size-input');
    var input_w = document.getElementById('width');
    var input_h = document.getElementById('height');
    if (x.style.display === 'none') {
      x.style.display = 'block';
      input_w.value = "720";
      input_h.value = '720';
    }
    else {
      x.style.display = 'none';
    }
  }
  
  function temp_9_16(){
    var x = document.getElementById('size-input');
    var input_w = document.getElementById('width');
    var input_h = document.getElementById('height');
    
    if (x.style.display === 'none') {
      x.style.display = 'block';
      input_w.value = "720";
      input_h.value = '1280';
    }
    else {
      x.style.display = 'none';
    }
  }
  
  function progress(){
    var x = document.getElementById('progress12')
    if (x.style.display === 'none'){
        x.style.display === 'block'
        $(".progress-bar").animate({
                    width: "95%",
            }, 2500);
    }
  }

  /* end templates */

