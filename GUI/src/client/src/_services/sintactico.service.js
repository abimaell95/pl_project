export const userService = {
    getAll
};


function getAll(string) {
    const requestOptions = {
        method: 'GET'
    };

    return fetch(`http://127.0.0.1:5000/parse?s=${string}`,requestOptions).then(handleResponse)
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                
                window.location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}