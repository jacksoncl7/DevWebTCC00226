$(function() {
  $( "#btn-id" ).click( function() {
    if ($( "#name-entry-id" ).val() != "") {
      new_row = "<tr><td class='name'>"+$( "#name-entry-id" ).val()+"</td><td> <button type='button' class='btn btn-primary move' name='button'>Mover</button></td></tr>"
      $( "#table-one tbody" ).append(new_row);
      $("#name-entry-id").val("");
    } else {
      $( "#name-entry-id" ).addClass( "is-invalid" );
    }
  } );

  $( "#btn-id" ).on( "click", function() {
    $( "#table-one tbody tr td button:first" ).click( function() {
      move_row = "<tr><td class='name'>" +
                 $( this ).parents("tr").children('.name').html() +
                 "</td><td> <button type='button' class='btn btn-primary move' name='button'>Excluir</button></td></tr>";
      $( this ).parents("tr").hide("slow");
      $( "#table-two tbody" ).append(move_row);

      $( "#table-two tbody tr td" ).on("click", "button", function() {
        $( this ).parents("tr").hide( "slow" );
      } );
     } );
   } );

   // $( "#table-one tbody tr td" ).on( "click", "button", function() {
   //   $( "#table-two tbody tr td" ).on("click", "button", function() {
   //     $( this ).parents("tr").hide( "slow" );
   //   } );
   //  } );


  $( "#name-entry-id" ).focus(function() {
    if ($("#name-entry-id").hasClass('is-invalid')) {
      $("#name-entry-id").removeClass( "is-invalid" );
    }
  });


});
