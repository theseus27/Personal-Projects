import React, { useState } from "react";
import Card from "@mui/material/Card";
import Page from "../../components";
import Chip from "@mui/material/Chip";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import CardActionArea from "@mui/material/CardActionArea";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import { useParams } from "react-router-dom";
import { useQuery } from "react-query";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";

const ShowOne  = () => {
  const { id } = useParams()
  const { data: result, isSuccess } = useQuery(`pokemon/${id}/`)

  console.log(result)

  if (!isSuccess) {
    return <div> Loading </div>;
  }

  return (
    <Page title="#{result.id}">
      <Container maxWidth="sm">
        <Typography color="primary" gutterBottom variant="h3">
          {result.name}
          {result.type1}
          {result.type2}
        </Typography>
        <img src={result.imgURL} alt=""/>
      </Container>
    </Page>
  );
};

export default ShowOne;
