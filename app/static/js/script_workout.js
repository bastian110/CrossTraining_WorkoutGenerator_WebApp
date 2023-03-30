document.getElementById("submit-button").addEventListener("click", function(event) {
    const sections = [
        { id: "equipement", className: "equipement-checkbox" },
        { id: "difficulty", className: "difficulty-checkbox" },
        { id: "duration", className: "duration-checkbox" },
        
        // Add more sections with their corresponding class names if needed
    ];

    for (let i = 0; i < sections.length; i++) {
        const checkboxes = document.getElementById(sections[i].id).getElementsByClassName(sections[i].className);
        let isChecked = false;

        for (let j = 0; j < checkboxes.length; j++) {
            if (checkboxes[j].checked) {
                isChecked = true;
                break;
            }
        }

        if (!isChecked) {
            event.preventDefault();
            alert(`Please select at least one checkbox in section ${i + 1}`);
            return;
        }
    }
});
