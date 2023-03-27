#include <fstream>
#include "export.h"

void exportToHTML(const std::string& fileName, const std::vector<Offer>& offers) {
	std::ofstream out(fileName, std::ios::trunc);
	if (!out.is_open()) throw RepoException{ "File " + fileName + " can't be opened\n" };
	out << "<html>" << std::endl;
	out << "<head><style>" << std::endl;
	out << "th, td {" << std::endl;
	out << "border-style:solid;" << std::endl;
	out << "border-color:#96D4D4; }" << std::endl;
	out << "</head></style>" << std::endl;
	out << "<body>" << std::endl;
	out << "<h1> Pachetul tarilor capitaliste </h1>" << std::endl;
	out << "<h2> Moisa approved! ;) </h2>" << std::endl;
	out << "<table style=\"width 100%\"><tr>" << std::endl;
	out << "<tr>" << std::endl;
	out << "<th> Denumire</th>" << std::endl;
	out << "<th> Destinatie</th>" << std::endl;
	out << "<th> Type</th>" << std::endl;
	out << "<th> Price</th>" << std::endl;
	out << "</tr>" << std::endl;
	for (const auto& ofr : offers) {
		out << "<tr>" << std::endl;
		out << "<td>" << ofr.getDenumire() << "</td>" << std::endl;
		out << "<td>" << ofr.getDestinatie() << "</td>" << std::endl;
		out << "<td>" << ofr.getType() << "</td>" << std::endl;
		out << "<td>" << ofr.getPrice() << "</td>" << std::endl;
		out << "</tr>" << std::endl;
	}
	out << "</tr></table>" << std::endl;
	//out << "<img src=\"moisa.jpg\" alt = \"Moisa\" width = \"1050\" height = \"500\">" << std::endl;
	out << "</body></html>" << std::endl;
}