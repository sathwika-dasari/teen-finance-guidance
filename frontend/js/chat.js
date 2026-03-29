// NetraOS Chat Widget Controller
document.addEventListener('DOMContentLoaded', () => {
    // Inject the widget HTML if it doesn't exist
    if (!document.getElementById('netra-widget-container')) {
        const widgetHTML = `
            <div id="netra-widget-container" class="netra-widget">
                <button id="netra-toggle-btn" class="netra-toggle">
                    BUDDY <span class="pulse"></span>
                </button>
                <div id="netra-chat-window" class="netra-window hidden">
                    <div class="netra-header">
                        <div class="netra-title">
                            <span class="status-dot"></span>
                            COMPANION V2.4
                        </div>
                        <button id="netra-close-btn" class="netra-close">X</button>
                    </div>
                    <div id="netra-messages" class="netra-messages">
                        <div class="netra-msg agent">
                            <span class="netra-sender">BUDDY:</span>
                            <span class="netra-text">Sensors online. Tactical guidance ready. State your inquiry.</span>
                        </div>
                    </div>
                    <form id="netra-input-form" class="netra-input-area">
                        <input type="text" id="netra-input" placeholder="Enter command..." autocomplete="off" />
                        <button type="submit" id="netra-send"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></button>
                    </form>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', widgetHTML);
    }

    const toggleBtn = document.getElementById('netra-toggle-btn');
    const closeBtn = document.getElementById('netra-close-btn');
    const chatWindow = document.getElementById('netra-chat-window');
    const messageContainer = document.getElementById('netra-messages');
    const inputForm = document.getElementById('netra-input-form');
    const inputField = document.getElementById('netra-input');
    const sendBtn = document.getElementById('netra-send');

    // Toggle Chat Window
    toggleBtn.addEventListener('click', () => {
        chatWindow.classList.toggle('hidden');
        if (!chatWindow.classList.contains('hidden')) {
            inputField.focus();
        }
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.classList.add('hidden');
    });

    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `netra-msg ${sender}`;
        
        const senderSpan = document.createElement('span');
        senderSpan.className = 'netra-sender';
        senderSpan.textContent = sender === 'agent' ? 'BUDDY:' : 'USER:';

        const textSpan = document.createElement('span');
        textSpan.className = 'netra-text';
        textSpan.textContent = text; // Escapes HTML natively

        msgDiv.appendChild(senderSpan);
        msgDiv.appendChild(textSpan);
        
        messageContainer.appendChild(msgDiv);
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }

    function addTypingIndicator() {
        const div = document.createElement('div');
        div.className = 'netra-msg agent typing-indicator';
        div.id = 'netra-typing';
        div.innerHTML = '<span class="netra-sender">BUDDY:</span><span class="netra-text">Analyzing<span class="dots">...</span></span>';
        messageContainer.appendChild(div);
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }

    function removeTypingIndicator() {
        const el = document.getElementById('netra-typing');
        if (el) el.remove();
    }

    inputForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const msg = inputField.value.trim();
        if (!msg) return;

        addMessage(msg, 'user');
        inputField.value = '';
        inputField.disabled = true;
        sendBtn.disabled = true;

        addTypingIndicator();

        try {
            // Wait for api.js implementation
            if (!API || !API.chat) {
                throw new Error("API.chat is not defined");
            }
            const res = await API.chat.sendMessage(msg);
            removeTypingIndicator();
            addMessage(res.response, 'agent');
        } catch (error) {
            removeTypingIndicator();
            console.error(error);
            addMessage("SYSTEM ERROR: Failed to communicate with main frame.", 'agent');
        } finally {
            inputField.disabled = false;
            sendBtn.disabled = false;
            inputField.focus();
        }
    });
});
