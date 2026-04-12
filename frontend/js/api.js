const API_BASE = '';
let _csrfToken = null;

async function getCSRFToken() {
    if (_csrfToken) return _csrfToken;
    try {
        const response = await fetch('/api/csrf_token');
        const data = await response.json();
        _csrfToken = data.csrf_token;
        return _csrfToken;
    } catch (e) {
        console.error("Could not fetch CSRF token", e);
        return null;
    }
}

async function apiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin'
    };

    if (['POST', 'PUT', 'DELETE'].includes(method.toUpperCase())) {
        const token = await getCSRFToken();
        if (token) {
            options.headers['X-CSRFToken'] = token;
        }
    }

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        
        // Handle no-content responses (like 204 or logout)
        if (response.status === 204 || endpoint.includes('logout')) {
            _csrfToken = null; // Clear token on logout
            return { message: 'Success' };
        }

        const result = await response.json();

        if (!response.ok) {
            // If CSRF failure, clear token and retry once
            if (response.status === 400 && result.message === 'The CSRF token is missing.') {
                _csrfToken = null;
                return apiRequest(endpoint, method, data);
            }
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
    learning: {
        getPath: () => apiRequest('/api/learning/path'),
        completeLesson: (data) => apiRequest('/api/learning/complete_lesson', 'POST', data),
        generateLesson: (data) => apiRequest('/api/learning/generate_lesson', 'POST', data)
    },

    // ✅ CHATBOT
    chat: {
        sendMessage: (message) => apiRequest('/api/chat', 'POST', { message })
    }
};