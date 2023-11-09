document.addEventListener("DOMContentLoaded", function() {
    // Code will run after the DOM has fully loaded

    $(document).ready(function() {
        $(".next-week").click(function() {
            var startOfWeek = $(this).data('start-of-week');
    
            var dateParts = startOfWeek.split('-');
            var year = dateParts[0];
            var month = dateParts[1] - 1;
            var day = dateParts[2];
            var startDate = new Date(year, month, day);
    
            startDate.setDate(startDate.getDate() + 7);
    
            var nextWeekUrl = "/calendar/?start_of_week=" + startDate.toISOString().slice(0, 10);
    
            window.location.href = nextWeekUrl;
        });
    });
    
});
