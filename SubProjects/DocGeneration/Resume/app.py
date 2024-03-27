from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    summary = request.form['summary']
    experience = request.form['experience'].split('\n')
    education = request.form['education'].split('\n')
    skills = request.form['skills'].split('\n')

    # Generate HTML resume
    html_resume = render_template('resume.html', 
                                  name=name, email=email, phone=phone,
                                  summary=summary, experience=experience,
                                  education=education, skills=skills)

    # Generate Markdown resume
    markdown_resume = f"# {name}\n\n" \
                      f"Email: {email}\n" \
                      f"Phone: {phone}\n\n" \
                      f"## Summary\n\n{summary}\n\n" \
                      f"## Experience\n\n" + '\n'.join([f"- {exp}" for exp in experience]) + '\n\n' \
                      f"## Education\n\n" + '\n'.join([f"- {edu}" for edu in education]) + '\n\n' \
                      f"## Skills\n\n" + '\n'.join([f"- {skill}" for skill in skills])

    return render_template('result.html', html_resume=html_resume, markdown_resume=markdown_resume)

if __name__ == '__main__':
    app.run(debug=True)
