$(function() {
  $('[data-toggle="tooltip"]').tooltip({
    boundary: 'window'
  });

  $('[data-toggle="popover"]').popover();

  //modalscript validations
  // document.querySelector("#nome").addEventListener("blur", function(e) {
  //   validateModalForm(e)
  // }, false);
  //
  document.querySelector("#sexo-fem").addEventListener("blur", function(e) {
    validateModalForm(e);
  }, false);

  // $('#modal-form-id').submit(function(event) {
  //   submitForm(event);
  // }, false);
  //
  // function submitForm(e) {
  //   e.preventDefault();
  //   nameIsValid();
  //   sexIsValid();
  // }

  function validateModalForm(e, form) {
    e.preventDefault();
    nameIsValid();
    sexIsValid();
  };

  function nameIsValid() {
    var name = $("#nome");
    if (name.val() === '') {
      name.addClass("is-invalid");
      name.removeClass("is-valid");
    } else {
      name.addClass("is-valid");
      name.removeClass("is-invalid");
    }
  }

  function sexIsvalid() {
    let maleCheck = $("#sexo-masc");
    let femaleCheck = $("#sexo-fem");
    if (maleCheck.prop('disebled') === femaleCheck.prop('disabled')) {
      maleCheck.addClass('is-invalid');
      femaleCheck.addClass('is-invalid');
    } else {
      maleCheck.addClass('is-invalid');
      femaleCheck.addClass('is-invalid');
    }
  }

  $("#btn1").click(function() {
    $('.card').addClass("border border-primary");
    $('.card-title').removeClass('text-center');
    $('#btn1').removeClass('btn-outline-primary');
    $('#btn1').addClass('btn-danger');
    $('img.card-img-top').addClass('rounded-pill mx-auto');
    $('img.card-img-top').width('80%');
  });

  $("#btn2").click(function() {
    $('.row img:first').addClass('rounded-pill');
    $('div.media img').addClass('shadow-lg p-3 mb-5 bg-white rounded');
    $('blockquote').wrap("<div class='overflow-auto mb-3'></div>");
    $("img[src*='.jpg'][alt^='Copa']").each(function() {
      // $(this).parent().find("div.card-body").after($(this));
      $(this).insertAfter($(this).parent().find("div.card-body"));
    });
  });

  $("#btn3").click(function() {
    // $("div.card div.card-body p:contains('cidade')").addClass('text-success');
    $("div.card div.card-body p").each(function() {
      if ($(this).text().toUpperCase().indexOf("CIDADE") > 0) {
        $(this).addClass("text-success");
      }
    })
    $("#btn3").html("Mais informações");
  })

  $("#btn4").click(function() {
    $("div.col-lg-6:first").insertAfter($("div.col-lg-6:last"));
  })

  $("#btn5").click(function() {
    var quantum = 0;
    $(this).append("...");
    $("div.card-body p:first").text("Novo texto do primeiro parágrafo.");
    $("div.card div.card-body p").each(function() {
      if ($(this).text().toUpperCase().indexOf("CIDADE") > 0) {
        quantum = quantum + 1;
        $(this).text("Novo texto do parágrafo (" + quantum + ")");
      }
    })
  });
  // Para atributos, há duas funções: attr() e removeAttr().
  // A função attr(nome) é usada para recuperar ou trocar o valor de um aributo.
  // Se o atributo não estiver presente então o resultado é undefined. Quando a
  // função é chamada com um valor - attr(nome, valor) - esse valor é designado
  // ao atributo.

  $("#btn6").click(function() {
    $("#cards").after("<h4 class='mb-3'>Lista de Imagens</h4> <ul id='imagens' class='list-group mb-4'>");
    $("img").each(function() {
      $("#imagens").append("<li class='list-group-item'>" + $(this).attr('alt') + "</li>");
    });
    //aplicar um hover sobre cada list-group-item aplicando a classe active
  })
});
