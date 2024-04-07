const express = require('express');
const PDFDocument = require('pdfkit');
const fs = require('fs');

const app = express();
app.use(express.json()); // For parsing application/json

app.post('/generate-leave-letter', (req, res) => {
    // Extracting new information from the request body
    const { 
        employeeName, 
        leaveDate, 
        reason, 
        endDate, 
        totalDays, 
        colleagueName, 
        email, 
        phoneNumber 
    } = req.body;

    // Create a PDF document
    const doc = new PDFDocument();
    let fileName = `Leave_Letter_${employeeName.replace(/\s/g, '_')}.pdf`;
    fileName = "./" + fileName; // Specify the file path

    // Pipe the PDF into a file
    doc.pipe(fs.createWriteStream(fileName));

    // Add the text with the newly added information
    doc.fontSize(14).text(`To Whom It May Concern,`, { underline: true });
    doc.moveDown();

    // Introduction
    doc.text(`I am writing to formally request a leave of absence for personal reasons. I have planned for this leave to commence on ${leaveDate} and conclude on ${endDate}, encompassing a total duration of ${totalDays} days.`, {
        lineGap: 2,
        paragraphGap: 5,
        indent: 20,
        align: 'justify',
    });

    doc.moveDown();

    // Detailed Explanation
    doc.text(`The reason for this leave is ${reason}, which requires my full attention during this period. I understand the impact my absence may have on the team and department operations, and thus, I have taken the necessary steps to mitigate any potential disruptions. I have prepared a detailed handover document and discussed my current projects with ${colleagueName}, who has kindly agreed to oversee my responsibilities during my absence. Furthermore, I have ensured that all my tasks are up to date, and I am committed to making the transition as smooth as possible.`, {
        lineGap: 2,
        paragraphGap: 5,
        indent: 20,
        align: 'justify',
    });

    doc.moveDown();

    // Conclusion and Contact Information
    doc.text(`I am hoping for your understanding and support regarding this matter and kindly request your approval for my leave application. Should you need to discuss this further, please feel free to contact me via email at ${email} or phone at ${phoneNumber}. I am willing to provide any additional information required and assist in any way possible to ensure a seamless transition.`, {
        lineGap: 2,
        paragraphGap: 5,
        indent: 20,
        align: 'justify',
    });

    doc.moveDown();
    doc.text(`Thank you for considering my request. I look forward to your positive response.`, {
        lineGap: 2,
        paragraphGap: 5,
        indent: 20,
        align: 'justify',
    });

    doc.moveDown();
    doc.text(`Sincerely,`, {
        lineGap: 4,
        align: 'left',
    });
    doc.text(`${employeeName}`, {
        lineGap: 4,
        align: 'left',
    });

    // Finalize the PDF and end the stream
    doc.end();

    // Send a response back
    res.send({ message: 'PDF generated successfully', fileName });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
