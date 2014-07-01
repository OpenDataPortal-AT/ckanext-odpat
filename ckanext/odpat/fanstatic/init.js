  $(function() {
      if ($('#socialshareprivacy').length > 0) {
          $('#socialshareprivacy').socialSharePrivacy({
              services: {
                  facebook: {
                      'dummy_img': '/socialshareprivacy/images/dummy_facebook.png'

                  },
                  twitter: {
                      'status': 'on',
                      'dummy_img': '/socialshareprivacy/images/dummy_twitter.png'
                  },
                  gplus: {
                      'dummy_img': '/socialshareprivacy/images/dummy_gplus.png'
                  }
              },
              'css_path': '/socialshareprivacy/socialshareprivacy.css',
              'lang_path': '/socialshareprivacy/lang/',
              'language': 'de'
          });
      }
        $("#field-begin_datetime").datetimepicker({
          changeMonth: true,
          changeYear: true,
          dateFormat: 'yy-mm-dd',
          showSecond: true,
          timeFormat: 'HH:mm:ss',
          separator: 'T'
        });
        $('#field-end_datetime' ).datetimepicker({
          changeMonth: true,
          changeYear: true,
          dateFormat: 'yy-mm-dd',
          showSecond: true,
          timeFormat: 'HH:mm:ss',
          separator: 'T'
        });
        $('#field-created' ).datepicker({
          changeMonth: true,
          changeYear: true,
          dateFormat: 'yy-mm-dd',
          showSecond: true,
          timeFormat: 'HH:mm:ss',
          separator: 'T'
        });
        $('#field-last_modified' ).datepicker({
          changeMonth: true,
          changeYear: true,
          dateFormat: 'yy-mm-dd',
          showSecond: true,
          timeFormat: 'HH:mm:ss',
          separator: 'T'
        });

        $('#field-license').on('change', function() {
          $('#license_link').attr('href', 'http://www.opendefinition.org/licenses/'+this.value);
          $('#license_link').html('opendefinition.org/licenses/'+this.value);
        });

        $('#license_link').attr('href', 'http://www.opendefinition.org/licenses/'+$('#field-license').val());
        $('#license_link').html('opendefinition.org/licenses/'+$('#field-license').val());

        $('#field-organization').on('change', function() {
          var text = $('#field-organization option:selected').text();
          if(text != 'Keine Organisation') {
            $('#field-publisher').attr('value', text);
          }
          else {
            $('#field-publisher').attr('value', '');
          }
        });

        if($('#field-organization')) {
          var text = $('#field-organization option:selected').text();
          if(text != 'Keine Organisation' && $('#field-publisher').val() == "") {
            $('#field-publisher').attr('value', text);
          }       
        }

        $('#field-publisher').on('keyup', function() {
          $('#field-organization option').removeAttr('selected');
          $('#field-organization').val('');
        });
  });


function openSummary()
      {
        $('#error_list').contents().remove();
        var isFormular = checkFormular();
        if(isFormular==true) {
/*          var erg = prompt("Änderungskommentar", document.getElementById('log_message').innerHTML);
          if(erg==null) {
            return false;
          }
          document.getElementById('log_message').innerHTML = erg;*/
          return true;
        }
        else {
          $('#error_div').show();
          var new_position = $('#error_div').offset();
          window.scrollTo(new_position.left,new_position.top);
          return false;
        }
      } 

      function checkFormular() {
        var formular = true;
/*        var elements = getElementsByClassName('dataset-create-form', 'div', document), n = elements.length;
        var isEditing = true;
        if(elements.length =='1') {
          isEditing = false;
        }*/
        if($('#field-title').val() == '') {
          formular = false;
          $('#error_list').append("<li>Bitte geben Sie einen Titel an.</li>");
        }
        
          if($('#field-categorization').val() == null) {
            formular = false;
            $('#error_list').append("<li>Bitte wählen Sie zumindestens eine Kategorie aus.</li>");
          }
          if($('#field-notes').val() == '') {
            formular = false;
            $('#error_list').append("<li>Bitte geben Sie eine Beschreibung ein.</li>");
          }
          if($('#field-maintainer').val() == '') {
            formular = false;
            $('#error_list').append("<li>Bitte geben Sie die Datenverantwortliche Stelle an.</li>");
          }
          if($('#field-name').val() == '') {
            formular = false;
            $('#error_list').append("<li>Bitte geben Sie eine Url an.</li>");
          }
          if($('#field-tag_string').val() == '') {
            formular = false;
            $('#error_list').append("<li>Bitte geben Sie zumindestens ein Schlagwort ein.</li>");
          }
          if($('#field-begin_datetime').val() == '') {
            formular = false;
            $('#error_list').append("<li>Bitte geben Sie die Zeitliche Ausdehnung (Anfang) an.</li>");
          }
        
        return formular;
      }
