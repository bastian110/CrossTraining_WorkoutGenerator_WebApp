
  document.querySelectorAll('[data-bs-toggle="modal"]').forEach((button) => {
    button.addEventListener('click', () => {
      const exerciseName = button.getAttribute('data-exercise-name');
      const modalLabel = document.querySelector('#executionDetailsModalLabel');
      const modalBody = document.querySelector('#executionDetailsModal .modal-body p');
      
      modalLabel.textContent = `Execution Details: ${exerciseName}`;
      modalBody.textContent = `Content for ${exerciseName} execution details goes here...`;
    });
  });
  
  
  