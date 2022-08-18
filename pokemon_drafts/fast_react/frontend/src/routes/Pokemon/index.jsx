import React from "react";
import { useQuery } from "react-query";
import { Link } from "react-router-dom";

import { styled } from "@mui/material/styles";
import Card from "@mui/material/Card";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import Page from "../../components"

const StyledLink = styled(Link)`
  text-decoration: none;
`;

const ShowAll  = () => {
  const { data: all, isSuccess } = useQuery("pokemon/");

  if (!isSuccess) {
    return <div>Loading</div>;
  }

  return (
    <Page title="All Pokemon">
      <Container maxWidth="sm">
        {all?.map((pokemon) => (
          <Box marginY={2}>
              <Card key={pokemon.id}>
                <Typography color="primary" gutterBottom variant="h3">
                  {pokemon.id}
                  {pokemon.name}
                </Typography>
              </Card>
          </Box>
        ))}
      </Container>
    </Page>
  );
};

export default ShowAll;
