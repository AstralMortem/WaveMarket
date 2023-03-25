$(document).ready(function () {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");

    });
});

//filter button click events
$(document).ready(function () {
    $("#filter-button").click(function () {
        $("#filter-column").toggleClass("is-hidden");
    });
});

$(".min-price").on("input", function() {
    value = $(this).val()
    $("#min-value").text(value + "$");
    $("#slider-min").val(value);
    $("#discount-slider-min").val(value);
 });

$(".max-price").on("input", function() {
    value = $(this).val()
    $("#max-value").text(value + "$");
    $("#slider-max").val(value);
    $("#discount-slider-max").val(value);
});

// Modal avatar
document.addEventListener('DOMContentLoaded', () => {
    // Functions to open and close a modal
    function openModal($el) {
      $el.classList.add('is-active');
    }
  
    function closeModal($el) {
      $el.classList.remove('is-active');
    }
  
    function closeAllModals() {
      (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
      });
    }
  
    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.modal-avatar-trigger') || []).forEach(($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);
  
      $trigger.addEventListener('click', () => {
        openModal($target);
      });
    });
  
    // Add a click event on various child elements to close the parent modal
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
      const $target = $close.closest('.modal');
  
      $close.addEventListener('click', () => {
        closeModal($target);
      });
    });
  
    // Add a keyboard event to close all modals
    document.addEventListener('keydown', (event) => {
      const e = event || window.event;
  
      if (e.keyCode === 27) { // Escape key
        closeAllModals();
      }
    });
  });
// Bulma message


bulmaToast.setDefaults({
    duration: 3000,
    position: 'top-center',
    closeOnClick: true,
  })

//order click show details
$(document).ready(function () {
  $("#order-card").each(function(){
    $(this).find("#order-detail-button").click(function (){
      $(this).find("#order-detail-card").toggleClass("is-hidden");
    })
  })
});


const buttons = document.querySelectorAll('#order-detail-button')

buttons.forEach(function(currentBtn){
  currentBtn.addEventListener('click', function (){
    var cls =currentBtn.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
    $(cls).find("#order-detail-card").toggleClass("is-hidden");
  });
});