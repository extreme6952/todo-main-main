document.addEventListener('DOMContentLoaded', function() {
    // Check if the status has changed
    if (document.querySelector('select[name="status"]').value === 'accepted') {
      // Update the status on the client-side
      document.querySelector('select[name="status"]').value = 'in_progress';
    }
  });