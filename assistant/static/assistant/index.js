// index.js
// function getCSRFToken() {
//   const name = 'csrftoken';
//   const cookies = document.cookie.split(';');
//   for (let cookie of cookies) {
//     cookie = cookie.trim();
//     if (cookie.startsWith(name + '=')) {
//       return decodeURIComponent(cookie.substring(name.length + 1));
//     }
//   }
//   return '';
// }

// document.addEventListener("DOMContentLoaded", () => {
//   const navLinks = document.querySelectorAll('.nav-link');

//   navLinks.forEach(link => {
//     link.addEventListener('click', () => {
//       const text = link.textContent.trim();

//       if (text.includes("Talk to NANI")) {
//         fetch("/start-assistant", {
//           method: "POST",
//           headers: {
//             "X-CSRFToken": getCSRFToken(),
//             "Content-Type": "application/json"
//           }
//         })
//         .then(response => {
//           if (!response.ok) {
//             throw new Error(`Status ${response.status}`);
//           }
//           return response.json();
//         })
//         .then(data => {
//           alert(data.status || "Started successfully!");
//         })
//         .catch(error => {
//           console.error("❌ Full Error:", error);
//           alert("❌ Assistant Error: " + error.message);
//         });
//       }
//     });
//   });
// });

// console.log('🤖 NANI-AI Assistant is ready!');





function getCSRFToken() {
  const name = 'csrftoken';
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    cookie = cookie.trim();
    if (cookie.startsWith(name + '=')) {
      return decodeURIComponent(cookie.substring(name.length + 1));
    }
  }
  return '';
}

document.addEventListener("DOMContentLoaded", () => {
  const navLinks = document.querySelectorAll('.nav-link');
  const chatArea = document.getElementById('chat-area');
  const listeningIndicator = document.getElementById('listening-indicator');

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      const text = link.textContent.trim();

      if (text.includes("Talk to NANI")) {
        listeningIndicator.style.display = "block";
        fetch("/start-assistant", {
          method: "POST",
          headers: {
            "X-CSRFToken": getCSRFToken(),
            "Content-Type": "application/json"
          }
        })
        .then(response => {
          listeningIndicator.style.display = "none";
          if (!response.ok) {
            throw new Error(`Status ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          if (data.conversation) {
            // Add a separator between conversations
            chatArea.innerHTML += `
              <div class="conversation-block">
                ${data.conversation.map(line => `<div>${line}</div>`).join('')}
              </div>
              <hr class="chat-separator">
            `;
            chatArea.scrollTop = chatArea.scrollHeight;
          }
        })
        .catch(error => {
          listeningIndicator.style.display = "none";
          alert("❌ Assistant Error: " + error.message);
        });
      }
    });
  });
});



// function getCSRFToken() {
//   const name = 'csrftoken';
//   const cookies = document.cookie.split(';');
//   for (let cookie of cookies) {
//     cookie = cookie.trim();
//     if (cookie.startsWith(name + '=')) {
//       return decodeURIComponent(cookie.substring(name.length + 1));
//     }
//   }
//   return '';
// }

// document.addEventListener("DOMContentLoaded", () => {
//   const navLinks = document.querySelectorAll('.nav-link');
//   const chatArea = document.getElementById('chat-area');
//   const listeningIndicator = document.getElementById('listening-indicator');
//   const naniAnimation = document.getElementById('nani-animation');

//   navLinks.forEach(link => {
//     link.addEventListener('click', () => {
//       const text = link.textContent.trim();

//       if (text.includes("Talk to NANI")) {
//         // 1. Show animation
//         naniAnimation.style.display = "flex";
//         listeningIndicator.style.display = "none";

//         // 2. Show self-introduction in chat
//         chatArea.innerHTML += `
//           <div class="conversation-block">
//             <div>🤖 Hi, I'm <b>NANI</b> – your personal voice assistant! How can I help you today?</div>
//           </div>
//           <hr class="chat-separator">
//         `;

//         // 3. Wait for 1.5s, then start listening
//         setTimeout(() => {
//           naniAnimation.style.display = "none";
//           listeningIndicator.style.display = "block";

//           fetch("/start-assistant", {
//             method: "POST",
//             headers: {
//               "X-CSRFToken": getCSRFToken(),
//               "Content-Type": "application/json"
//             }
//           })
//           .then(response => {
//             listeningIndicator.style.display = "none";
//             if (!response.ok) {
//               throw new Error(`Status ${response.status}`);
//             }
//             return response.json();
//           })
//           .then(data => {
//             if (data.conversation) {
//               chatArea.innerHTML += `
//                 <div class="conversation-block">
//                   ${data.conversation.map(line => `<div>${line}</div>`).join('')}
//                 </div>
//                 <hr class="chat-separator">
//               `;
//               chatArea.scrollTop = chatArea.scrollHeight;
//             }
//           })
//           .catch(error => {
//             listeningIndicator.style.display = "none";
//             alert("❌ Assistant Error: " + error.message);
//           });
//         }, 1500);
//       }
//     });
//   });
// });