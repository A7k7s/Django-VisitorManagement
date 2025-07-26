// Set date range to future 10 days only
  const dateField = document.getElementById("dateField");
  const today = new Date();
  const minDate = new Date(today.setDate(today.getDate() + 1));
  const maxDate = new Date(minDate);
  maxDate.setDate(minDate.getDate() + 9);

  dateField.min = minDate.toISOString().split("T")[0];
  dateField.max = maxDate.toISOString().split("T")[0];

  // Optional: file size check (2MB max)
  document.getElementById("visitorForm").addEventListener("submit", function(e) {
    const file = document.querySelector("input[type='file']").files[0];
    if (file && file.size > 2 * 1024 * 1024) {
      e.preventDefault();
      alert("File size must be less than or equal to 2MB");
    }
  });

  // Show popup if success flag is present
window.addEventListener("DOMContentLoaded", () => {
  const success = document.getElementById("success-flag");
  if (success) {
    alert("Successfully submitted!");
    document.getElementById("visitorForm").reset();
  }
});
document.addEventListener("DOMContentLoaded", function () {
  flatpickr("#timeInput", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",     // 24-hour format: Hour:Minute (e.g., 14:30)
    minTime: "09:00",      // Minimum time: 09:00
    maxTime: "17:00",      // Maximum time: 17:00
    time_24hr: true        // Enable 24-hour format
  });
});

