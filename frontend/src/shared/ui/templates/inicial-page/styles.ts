import { motion } from 'framer-motion'
import styled from "styled-components"

export const GlobalContainer = styled.div`
  width: 100vw;
  height: 100vh;
`

export const Container = styled.div`
  height: calc(100% - 4.8rem);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3.5rem;
`

export const WrapperBrandButtons = styled.div`
  display: flex;
  gap: 1.5rem;
`

export const WrapperTitleAndSubTitle = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.2rem;
`

export const ConfirmButton = styled(motion.button)`
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;

  border-radius: 1.2rem;
  width: 48rem;
  height: 4.8rem;
  padding: 2rem;

  color: #FFFFFF;
  background-color: #2B8FE3;

  font-size: 1.6rem;
  font-family: 'Public Sans', sans-serif;
  font-weight: 700;
  line-height: 2.4rem;
`