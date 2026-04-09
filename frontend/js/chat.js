// TeenFinance Interactive Chat Widget Controller
document.addEventListener('DOMContentLoaded', () => {
    // Inject the widget HTML if it doesn't exist
    if (!document.getElementById('chat-widget-container')) {
        const timeNow = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        
        const widgetHTML = [
            '<div id="chat-widget-container" class="chat-widget">',
                '<button id="chat-toggle-btn" class="chat-fab">',
                    '<i class="fas fa-robot"></i>',
                '</button>',
                '<div id="chat-window" class="chat-window hidden">',
                    '<div class="chat-header">',
                        '<div class="chat-avatar-top">',
                            '<i class="fas fa-robot"></i>',
                        '</div>',
                        '<h3 class="chat-title">Teen Finance Assistant</h3>',
                        '<p class="chat-subtitle">Ask anything about finance</p>',
                        '<button class="chat-learn-more" onclick="window.location.href=\'/internships\'">Learn More</button>',
                    '</div>',
                    
                    '<div class="chat-body-container">',
                        '<div id="chat-messages" class="chat-messages">',
                            '<div class="chat-timestamp">Today, ' + timeNow + '</div>',
                            
                            '<!-- Initial Bot Message -->',
                            '<div class="chat-msg-row agent">',
                                '<div class="chat-msg-avatar"><i class="fas fa-robot"></i></div>',
                                '<div class="chat-bubble">',
                                    'Hi 👋 I\'m your finance assistant!',
                                '</div>',
                            '</div>',
                            
                            '<!-- Quick Action Pills -->',
                            '<div class="chat-quick-actions" id="chat-quick-actions">',
                                '<button class="chat-pill">Find Internships</button>',
                                '<button class="chat-pill">Safety Tips</button>',
                                '<button class="chat-pill">System Help</button>',
                                '<button class="chat-pill">Career Paths</button>',
                            '</div>',
                        '</div>',
                        
                        '<form id="chat-input-form" class="chat-input-area">',
                            '<input type="text" id="chat-input" class="chat-input" placeholder="Type and press [enter]" autocomplete="off" />',
                            '<div class="chat-actions">',
                                '<i class="far fa-smile"></i>',
                                '<i class="fas fa-paperclip"></i>',
                                '<button type="submit" id="chat-send" class="chat-send-btn">',
                                    '<i class="fas fa-paper-plane" style="font-size: 14px;"></i>',
                                '</button>',
                            '</div>',
                        '</form>',
                    '</div>',
                '</div>',
            '</div>'
        ].join('');
        document.body.insertAdjacentHTML('beforeend', widgetHTML);
    }

    const toggleBtn = document.getElementById('chat-toggle-btn');
    const chatWindow = document.getElementById('chat-window');
    const messageContainer = document.getElementById('chat-messages');
    const inputForm = document.getElementById('chat-input-form');
    const inputField = document.getElementById('chat-input');
    const sendBtn = document.getElementById('chat-send');
    const quickActions = document.getElementById('chat-quick-actions');
    const pills = document.querySelectorAll('.chat-pill');
    
    // Toggle Chat Window
    toggleBtn.addEventListener('click', () => {
        chatWindow.classList.toggle('hidden');
        if (!chatWindow.classList.contains('hidden')) {
            inputField.focus();
        }
    });

    function addMessage(text, sender) {
        const msgRow = document.createElement('div');
        msgRow.className = 'chat-msg-row ' + sender;
        
        let avatarHTML = '';
        if (sender === 'agent') {
            avatarHTML = '<div class="chat-msg-avatar"><i class="fas fa-robot"></i></div>';
        }

        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble';
        
        // Advanced formatting
        let formattedText = text
            .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>')
            .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" style="color: inherit; text-decoration: underline; font-weight: bold;">$1</a>');
            
        // Basic bullet points handler
        if (formattedText.includes('\n- ') || formattedText.includes('\n* ')) {
            formattedText = formattedText.replace(/^[-*] (.*$)/gim, '<li>$1</li>');
            formattedText = formattedText.replace(/(<li>.*<\/li>)/sim, '<ul>$1</ul>');
        } else if (formattedText.trim().startsWith('- ') || formattedText.trim().startsWith('* ')) {
             formattedText = formattedText.replace(/^[-*] (.*$)/gim, '<li>$1</li>');
             formattedText = '<ul>' + formattedText + '</ul>';
        }

        bubble.innerHTML = formattedText.replace(/\n/g, '<br>').replace(/<\/ul><br>/g, '</ul>');

        if (sender === 'agent') {
            msgRow.innerHTML = avatarHTML;
            msgRow.appendChild(bubble);
        } else {
            msgRow.appendChild(bubble);
        }
        
        messageContainer.appendChild(msgRow);
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }

    function addTypingIndicator() {
        const div = document.createElement('div');
        div.className = 'chat-msg-row agent typing-indicator';
        div.id = 'chat-typing';
        div.innerHTML = '<div class="chat-msg-avatar"><i class="fas fa-robot"></i></div>' +
            '<div class="chat-bubble chat-dots"><span></span><span></span><span></span></div>';
        messageContainer.appendChild(div);
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }

    function removeTypingIndicator() {
        const el = document.getElementById('chat-typing');
        if (el) el.remove();
    }

    async function handleMessageSubmit(msg) {
        if (!msg) return;

        // Hide quick actions once chat begins (keep them visible for the first interaction)
        // if (quickActions) quickActions.style.display = 'none';

        addMessage(msg, 'user');
        inputField.value = '';
        inputField.disabled = true;
        sendBtn.disabled = true;
        sendBtn.classList.remove('active');

        addTypingIndicator();

        try {
            if (!API || !API.chat) throw new Error("API.chat is not defined");
            const res = await API.chat.sendMessage(msg);
            
            // Artificial delay for "thinking" feel
            await new Promise(r => setTimeout(r, 600));
            
            removeTypingIndicator();
            addMessage(res.response, 'agent');
        } catch (error) {
            removeTypingIndicator();
            console.error(error);
            addMessage("Apologies! COMPANION is having a minor connection issue. Please try again later.", 'agent');
        } finally {
            inputField.disabled = false;
            sendBtn.disabled = false;
            inputField.focus();
        }
    }

    // Input submit
    inputForm.addEventListener('submit', (e) => {
        e.preventDefault();
        handleMessageSubmit(inputField.value.trim());
    });
    
    // Quick pills clicking
    pills.forEach(pill => {
        pill.addEventListener('click', (e) => {
            const query = e.target.textContent;
            inputField.value = query;
            handleMessageSubmit(query);
        });
    });

    // Button active state logic
    inputField.addEventListener('input', () => {
        if (inputField.value.trim().length > 0) {
            sendBtn.classList.add('active');
        } else {
            sendBtn.classList.remove('active');
        }
    });
});
