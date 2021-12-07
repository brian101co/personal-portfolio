$(document).ready(() => {
  $('a[href*="#"]')
      .not('[href="#"]')
      .not('[href="#0"]')
      .click(function(event) {
        if (
          location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
          && 
          location.hostname == this.hostname
        ) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
          if (target.length) {
            event.preventDefault();
            $('html, body').animate({
              scrollTop: target.offset().top
            }, 700, function() {
              var $target = $(target);
              if ($target.is(":focus")) { 
                return false;
              } else {
                $target.attr('tabindex','-1');
              };
            });
          }
        }
      });

    setTimeout(() => {
      $('.alert').remove()
    }, 3000)

    const carouselItemHeights = [];
    $('.carousel-inner').each(function() {
      carouselItemHeights.push($(this).outerHeight());
    });
    $('.carousel-inner .slider').css("height", Math.max(...carouselItemHeights));
});

function loadStyleSheet() {
  const stylesheet = document.querySelector('link[media="print"]');
  stylesheet.media = "all";
}

window.onload = function () {
  loadStyleSheet();
}
