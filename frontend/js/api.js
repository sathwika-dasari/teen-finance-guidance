const API_BASE = '/api';

async function apiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        }
    };

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
        register: (userData) => apiRequest('/auth/register', 'POST', userData),
        login: (credentials) => apiRequest('/auth/login', 'POST', credentials),
        logout: () => apiRequest('/auth/logout', 'POST'),
        updateProfile: (data) => apiRequest('/auth/update_profile', 'POST', data)
    },
    recommendation: {
        getGuidance: () => apiRequest('/recommendation/get_guidance'),
        getLesson: (id) => apiRequest(`/recommendation/get_lesson/${id}`)
    },
    dashboard: {
        getProgress: () => apiRequest('/dashboard/progress'),
        updateProgress: (progressData) => apiRequest('/dashboard/update_progress', 'POST', progressData)
    }
};
