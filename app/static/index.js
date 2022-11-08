function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteAllNotes() {
  fetch("/delete_all_notes", {
    method: "POST",
    body: JSON.stringify({}),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function openNotes() {
  fetch("/open_notes", {
    method: "POST",
    body: JSON.stringify({}),
  }).then((_res) => {
  });
}