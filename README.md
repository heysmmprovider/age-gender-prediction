# Age and Gender Prediction API

<img src="https://cdn.mypanel.link/h1sa68/zwquifzpzxn5h5tc.png" alt="HeySmmReseller Logo" style="width: 100%;">

Welcome to the Age and Gender Prediction API repository! This project builds easy-to-use REST API for seamless integration into your applications.

## About
This project is maintained and powered by **HeySMMProvider** and its sub-brand **HeySMMReseller**.

- **HeySMMProvider**: Your go-to provider for top-tier social media services, supporting all major platforms to help you or your business shine online.
- **HeySMMReseller**: We enhance these services with exceptional customer support and affordable provider prices, ensuring our solutions work for everyone.

For more details, visit our website: [heysmmreseller.com](https://heysmmreseller.com)

## Features
- Easy REST API interface for predicting age and gender from images.
- Flexible deployment with Docker support.
- GPU acceleration for high-performance inference.

## How to Use
### 1. Build the Docker Image
To build your own Docker image, use the following command:

```bash
docker build -f Dockerfile-our -t age-gender-prediction .
```

### 2. Run the Docker Container
Use our prebuilt Docker container for quick and hassle-free deployment:

```bash
docker run -it --gpus all -e LISTEN_PORT=5001 -p 5001:5001 heysmmprovider/age-gender-prediction-by-heysmmreseller:v1.0.0
```

You can find our container on Docker Hub: [Docker Hub Link](https://hub.docker.com/repository/docker/heysmmprovider/age-gender-prediction-by-heysmmreseller/general)

## API Usage Example
Below is an example of how to use the API for predictions. This example assumes the server is running on `http://localhost:5001/`:

### Client Code
```javascript
async predictFromApi(image_url) {
    try {
        console.log('Fetching image:', image_url);
        const base64String = await this.fetchImageAsBase64(image_url);

        const payload = {
            img: [`data:image/jpeg;base64,${base64String}`]
        };

        const response = await fetch('http://YOUR_API_ENDPOINT/', {
            method: 'POST',
            body: JSON.stringify(payload),
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'text/plain'
            }
        });
        const json = await response.json();
        console.log('API Response:', json);
        return {
            prediction_error: false,
            data: json
        };
    } catch (error) {
        console.error('Error in predictFromApi:', error.message);
        return {
            prediction_error: true,
            error: error.message
        };
    }
}
```

### Example Response
```json
{
  "ages": [
    { "entropy": 0.7372506851631059, "mean": 16.158203125 }
  ],
  "genders": [
    { "entropy": 0.025559460044411432, "f": 0.99609375, "m": 0.00390625 }
  ]
}
```

## Contribution
We welcome contributions to improve this project! Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss your ideas.

## License
This project is licensed under the MIT License.

---

Thank you for using **HeySMMProvider** and **HeySMMReseller** to power your projects! Together, we deliver innovative solutions and support your goals.

