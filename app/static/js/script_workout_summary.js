document.querySelectorAll('[data-bs-toggle="modal"]').forEach((button) => {
  button.addEventListener('click', () => {
    const exerciseName = button.getAttribute('data-exercise-name');
    const videoUrl = button.getAttribute('data-video-url');

    const modalLabel = document.querySelector('#executionDetailsModalLabel');
    const modalBody = document.querySelector('#executionDetailsModal .modal-body p');
    const videoIframe = document.getElementById('videoIframe');

    modalLabel.textContent = `Execution Details: ${exerciseName}`;
    modalBody.textContent = `Content for ${exerciseName} execution details goes here...`;
    videoIframe.src = videoUrl;
  });
});

const executionDetailsModal = document.getElementById('executionDetailsModal');
executionDetailsModal.addEventListener('hidden.bs.modal', (event) => {
  const videoIframe = document.getElementById('videoIframe');
  videoIframe.src = ''; // Clear the src attribute when the modal is closed
});
