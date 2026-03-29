const API_BASE = '';

async function apiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'login'.includes('login') ? 'same-origin' : 'include' // safe same-origin
    };
    options.credentials = 'same-origin';

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message || 'Something went wrong');
        }

        return result;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

const API = {
    auth: {
        register: (userData) => apiRequest('/api/auth/register', 'POST', userData),
        login: (credentials) => apiRequest('/api/auth/login', 'POST', credentials),
        logout: () => apiRequest('/api/auth/logout', 'POST'),
        updateProfile: (data) => apiRequest('/api/auth/update_profile', 'POST', data)
    },
    recommendation: {
        getGuidance: () => apiRequest('/api/recommendation/get_guidance'),
        getLesson: (id) => apiRequest(`/api/recommendation/get_lesson/${id}`)
    },
    dashboard: {
        getProgress: () => apiRequest('/api/dashboard/progress'),
        updateProgress: (progressData) => apiRequest('/api/dashboard/update_progress', 'POST', progressData)
    },

    // ✅ CHATBOT
    chat: {
        sendMessage: (message) => apiRequest('/chat', 'POST', { message })
    }
};