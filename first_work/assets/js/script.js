$(function() {
  $('body').scrollspy();  //JQuery var scrolling used JS, specify scrollspy from bootstrap.js

  $('[data-toggle="tooltip"]').tooltip({
    boundary: 'window'
  });

  $('[data-toggle="popover"]').popover();

  liker();

  function liker() {
    var num_like = $("#like").data("like");
    var num_dislike = $("#dislike").data("dislike");
    $("#like").addClass("badge badge-light").html(num_like);
    $("#dislike").addClass("badge badge-light").html(num_dislike);
    $("#pos").click(function() {
      if ($('#ineg').hasClass('far')) {
        $('#ineg').removeClass('fas');
        num_dislike = num_dislike - 1;
        }
      if ($('#ipos').hasClass('fas')) {
        $('#ipos').removeClass('fas');
        num_like = num_like - 1;
      } else {
        $('#ipos').addClass('fas');
        num_like = num_like + 1;
      }
    });
    $('#neg').click(function() {
      if ($('#ipos').hasClass('far')) {
        $('#ipos').removeClass('fas');
        num_like = num_like - 1
        }
      if ($('#ineg').hasClass('fas')) {
        $('#ineg').removeClass('fas');
        num_dislike = num_dislike - 1
      } else {
        $('#ineg').addClass('fas');
        num_dislike = num_dislike + 1
      }
    });
  }
  // 18:15 SPA UFF
  // $('a.nav-link.nav-item').mouseenter(function() {
  //    $('a.nav-link.nav-item').removeClass('active');
  //    $(this).addClass('active');
  // });
  //
  // $('a.nav-link.nav-item').not(".dropdown-toggle").click(function() {
  //    $('div.collapse.navbar-collapse').removeClass('show');
  // });
  //
  // $('a.dropdown-item').click(function() {
  //    $('div.collapse.navbar-collapse').removeClass('show');
  // });
  //
  // $('a.nav-link.nav-item').mouseleave(function() {
  //      $(this).removeClass('active');
  //   });
});
