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
      if ($('#ineg').hasClass('far') && $('#ipos').hasClass('fas')) {
        $('#ipos').removeClass('fas');
        $('#ipos').addClass('far');
        num_like -= 1;
      } else if ($('#ineg').hasClass('far') && $('#ipos').hasClass('far')) {
        $('#ipos').removeClass('far');
        $('#ipos').addClass('fas');
        num_like += 1;
      } else if ($('#ineg').hasClass('fas') && $('#ipos').hasClass('far')) {
        $('#ineg').removeClass('fas');
        $('#ineg').addClass('far');
        $('#ipos').removeClass('far');
        $('#ipos').addClass('fas');
        num_like += 1;
        num_dislike -= 1;
      }
      $("#like").addClass("badge badge-light").html(num_like);
      $("#dislike").addClass("badge badge-light").html(num_dislike);
    });
    $('#neg').click(function() {
      if ($('#ineg').hasClass('far') && $('#ipos').hasClass('far')) {
        $('#ineg').removeClass('far');
        $('#ineg').addClass('fas');
        num_dislike += 1;
      } else if ($('#ineg').hasClass('fas') && $('#ipos').hasClass('far')) {
        $('#ineg').removeClass('fas');
        $('#ineg').addClass('far');
        num_dislike -= 1;
      } else if ($('#ineg').hasClass('far') && $('#ipos').hasClass('fas')) {
        $('#ineg').removeClass('far');
        $('#ineg').addClass('fas');
        $('#ipos').removeClass('fas');
        $('#ipos').addClass('far');
        num_dislike += 1;
        num_like -= 1;
      }
      $("#like").addClass("badge badge-light").html(num_like);
      $("#dislike").addClass("badge badge-light").html(num_dislike);
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
